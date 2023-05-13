import os
import re
import sys
import math
import argparse
import faulthandler
faulthandler.enable()
from sklearn.metrics import roc_auc_score
from utils.other_utils import load_story, write_to_file, create_folder, log_inconsistency, get_gpt3_response, check_GPT_res, log_prediction, get_codex_response, check_codex_res
from utils.world_checker_utils import get_world_model, majority_vote, transform_to_description
from utils.world_tracker_utils import tracker_codex_comment, tracker_codex_function, tracker_codex_abstract
from utils.prompts import *

import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification, AutoModelForTokenClassification, AutoModelForQuestionAnswering, T5TokenizerFast, T5ForConditionalGeneration
device='cuda' if torch.cuda.is_available() else 'cpu'
entailment_model = AutoModelForSequenceClassification.from_pretrained('facebook/bart-large-mnli').to(device)
entailment_tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-mnli')

def get_args_parser():
    parser = argparse.ArgumentParser('re3', add_help=False)
    parser.add_argument('--track', action='store_true')
    parser.add_argument('--check', action='store_true')
    
    parser.add_argument('--story_folder_path', default='./re3_stories', type=str)
    parser.add_argument('-p', '--folder_path', default='./re3_exp', type=str)
    parser.add_argument('-t', '--world_tracker_mode', default='Codex_abstract', type=str)  ## Choices are Codex_abstract, Codex_comment, Codex_function
    parser.add_argument('-c', '--world_checker_mode', default='TE', type=str)  ## Choices are TE (Textual Entailment), GPT3_all_attr, GPT3_one_attr, Codex_one_attr 
    parser.add_argument('-n', '--num_generation', default=3, type=int)
    parser.add_argument('-s', '--start_index', default=0, type=int)
    parser.add_argument('-e', '--end_index', default=100, type=int)
    
    return parser

def score_entailment(premise, hypothesis):
    """
    Score entailment between two sentences
    """
    premise = [premise] if type(premise) == str else premise
    hypothesis = [hypothesis] if type(hypothesis) == str else hypothesis
    batch_inputs = entailment_tokenizer(premise, hypothesis, return_tensors='pt', padding=True)
    batch_inputs = {key:value.to(entailment_model.device) for key, value in batch_inputs.items()}
    logprobs = entailment_model(**batch_inputs).logits.log_softmax(dim=-1)
    consistent_logprobs = logprobs[:, 1:].logsumexp(dim=1) # log probability of not contradictory (contradiction is index 0)
    penalty = (-consistent_logprobs).max().item()
    return logprobs.detach().cpu().numpy()[0][0]

def check_rel_same_char(premise, hypo):
    if 'of' in premise and 'of' in hypo:
        premise_char_1 = premise.split("of")[1].strip()
        hypo_char_1 = hypo.split("of")[1].strip()
        premise_char_2 = premise.split("is")[0].strip()
        hypo_char_2 = hypo.split("is")[0].strip()
        
        return ((premise_char_1==hypo_char_1) and (premise_char_2==hypo_char_2))
    else:
        return True

### Codex_prompt_1, GPT3_prompt_1 --> directly read and check if consistent/inconsistent is in the response
### Codex_prompt_2, Codex_prompt_3 --> import the World model --> use TE, GPT3_all_attr, GPT3_one_attr to check
### TO-DO: GPT3_prompt_2, GPT3_prompt_3 --> parse out GPT3 json output --> use TE, GPT3_all_attr, GPT3_one_attr to check
### Other than these, we have the  baseline from Re3 paper: (story-level) Entailment, (sentence-level) Entailment-DPR, Open-IE-based Structured-Detect

def world_tracker(args):
    print('start world tracker')
    for story_idx in range(60):
        if story_idx > args.end_index:
            continue
        oringinal_info, altered_info, original_story, altered_story = load_story(story_idx, args)
        if original_story == None:
            continue
        
        consistency_story_list = [('consistent_1', oringinal_info, original_story), ('consistent_2', altered_info, altered_story), 
                                ('inconsistent_1', oringinal_info, altered_story), ('inconsistent_2', altered_info, original_story)]
        
        ## Iterate through consistent and inconsistent combo of stories
        print('start')
        for (story_type, info, story) in consistency_story_list:
            sub_folder = os.path.join(args.folder_path, args.world_tracker_mode)
            subsubfolder = os.path.join(args.folder_path, sub_folder, 'story_' + str(story_idx))
            if not os.path.exists(subsubfolder):
                os.mkdir(subsubfolder)
            
            for gen_count in range(args.num_generation):
                for story_or_setting in ['story_setting', 'story']:
                    output_path = os.path.join(subsubfolder, f"{story_type}_{gen_count}_{story_or_setting}.py")
                    print(output_path)
                    if args.world_tracker_mode == 'Codex_comment':
                        output = tracker_codex_comment(info, story, story_or_setting, sub_folder, subsubfolder, output_path)
                    elif args.world_tracker_mode == 'Codex_function':
                        output = tracker_codex_function(info, story, story_or_setting, sub_folder, subsubfolder, output_path)
                    elif args.world_tracker_mode == 'Codex_abstract':
                        output = tracker_codex_abstract(info, story, story_or_setting, sub_folder, subsubfolder, output_path)
                    else:
                        print(f"invalid world_tracker_mode {args.world_tracker_mode}")
                    # write_to_file(output, sub_folder, subsubfolder, output_path)

def world_checker(args):
    y_truth, y_pred = [], []  ## 0 for consistent story, 1 for inconsistent story
    sub_folder = os.path.join(args.folder_path, args.world_tracker_mode)
    print('start')
    
    for story_idx in os.listdir(sub_folder):
        _, tmp = story_idx.split('_')
        if tmp.isdigit() and int(tmp) < args.start_index:
            print(f"skipping {story_idx}")
            continue
        subsubfolder = os.path.join(sub_folder, story_idx)
        if subsubfolder.endswith("txt"):
            continue
        
        for story_type in ['consistent_1', 'consistent_2', 'inconsistent_1', 'inconsistent_2']:
            print(f"{story_idx}: {story_type}")
            story_world_list, story_setting_world_list = [], []
            for file_name in os.listdir(subsubfolder):
                # print(file_name)
                try:
                    if file_name.startswith(story_type) and '__pycache__' not in file_name and 'log' not in file_name:
                        world = get_world_model(file_name, subsubfolder)
                        # print(file_name)
                        if 'story_setting' in file_name:
                            world.story()
                            story_setting_world_list.append(world)
                        elif 'story' in file_name and 'story_setting' not in file_name:
                            world.story()
                            story_world_list.append(world)
                except KeyboardInterrupt:
                    sys.exit(0)
                except Exception as e:
                    print(e)     
            try:
                if args.world_checker_mode == 'GPT-3':
                    # print(len(story_world_list), len(story_setting_world_list))
                    story_world = transform_to_description(majority_vote(story_world_list))
                    story_setting_world = transform_to_description(majority_vote(story_setting_world_list))
                    total_inconsistency = 0
                    for char_name in story_world.keys():
                        char_desc_story = ' '.join(story_world[char_name])
                        char_desc_setting =' '.join(story_setting_world[char_name])
                        # print(story_world)
                        log_file_path = os.path.join(subsubfolder,f'{story_type}_log.txt')
                        log_prediction('\n\nSTORY: ' + char_desc_story, log_file_path)
                        log_prediction('\nSETTING:' + char_desc_setting, log_file_path)
                        
                        prompt = f"Question: Are there any contradiction in the person's description? \nStory Setting: {char_desc_story}  \nStory: {char_desc_setting} \nAnswer:"
                        res = get_gpt3_response(GPT3_consistency_prompt_3 + prompt, max_tokens = 200) 
                        log_prediction('\nres\n' + res, log_file_path)
                        inconsistency_count = re.findall(r'\d+', res)
                        total_inconsistency += int(inconsistency_count[-1])
                        print(str(total_inconsistency) + '      '  + res)

                    ## record the prediction
                    y_pred.append(total_inconsistency)
                    label = 1 if 'inconsistent' in file_name else 0
                    y_truth.append(label)
                    print(os.path.join(sub_folder,'log.txt'))
                    log_prediction(f"{story_idx} {story_type}: {total_inconsistency}\n",  os.path.join(sub_folder,'log.txt'))
                
                elif args.world_checker_mode == 'TE':
                    print(len(story_world_list), len(story_setting_world_list))
                    story_world = transform_to_description(majority_vote(story_world_list))
                    story_setting_world = transform_to_description(majority_vote(story_setting_world_list))
                    log_file_path = os.path.join(subsubfolder,f'{story_type}_TE_log.txt')
                    max_contradition_prob = 0
                    for char_name in story_world.keys():
                        char_desc_story = story_world[char_name]
                        char_desc_setting = story_setting_world[char_name]
                        for premise in char_desc_setting:
                            for hypo in char_desc_story:
                                # contradiction_prob = TE_model.predict(premise, hypo)['label_probs'][1]
                                ## if A is the X of B. and A is the Y of B
                                ## check_rel_same_char is true when B and B.
                                if not check_rel_same_char(premise, hypo) and 'of' in premise and 'of' in hypo:
                                    print('skip this', premise, hypo)
                                    pass
                                else:
                                    contradiction_prob = math.exp(score_entailment(premise, hypo))
                                    log_prediction(f"premise: {premise}\n hypo:{hypo}\n contradition: {contradiction_prob}\n\n" , log_file_path)
                                    if contradiction_prob > max_contradition_prob:
                                        max_contradition_prob = contradiction_prob
                                        contradition_premise, contradition_hypo = premise, hypo
                    
                    ## record the prediction        
                    log_prediction(f"\nMAX_PROB is {max_contradition_prob}\nCONTRADICTORY_PREMISE: {contradition_premise}\n CONTRADICTORY_HYPO: {contradition_hypo}" , log_file_path)
                    y_pred.append(max_contradition_prob)
                    label = 1 if 'inconsistent' in story_type else 0
                    y_truth.append(label)
                    print(os.path.join(sub_folder,'log.txt'))
                    log_prediction(f"{story_idx} {story_type}: {max_contradition_prob}\n",  os.path.join(sub_folder,'TE_log.txt'))
            except Exception as e:
                print(e) 
    
    ## record the final AUC scure
    auc = roc_auc_score(y_truth, y_pred)
    log_prediction(f'\n\nFinal AUC {auc} for tracker {args.world_tracker_mode} checker {args.world_checker_mode}', os.path.join(sub_folder,'TE_log.txt'))

if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()
    
    print(f'program start with {args.world_tracker_mode} {args.world_checker_mode}')
    if args.track:
        create_folder(args)
        world_tracker(args)
        
    if args.check:
        world_checker(args)