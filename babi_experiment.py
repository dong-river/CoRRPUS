import os
import json
import argparse
import numpy as np
import pandas as pd

from utils.other_utils import dump_to_json, get_gpt3_response, get_codex_response, text_to_code
from utils.babi_prompts import *
from utils.babi_utils import *

def get_args_parser():
    parser = argparse.ArgumentParser('babi', add_help=False)

    parser.add_argument('-i', '--input_dir', default='./babi/tasks', type=str)
    parser.add_argument('-o', '--output_dir', default='./babi/codex', type=str)
    parser.add_argument('--task', default='2', type=str, help="otherwise pass in something like 1,2,3")    ## do one task in each run
    parser.add_argument('-t', '--world_tracker_mode', default='all', type=str)  ## Choices are GPT3, Codex_raw, Codex_comment, Codex_command, Codex_symbolic, GPT_comment, GPT_command, GPT_symbolic, all
    parser.add_argument('--track', action='store_true')
    parser.add_argument('--check', action='store_true')
    parser.add_argument('-m', '--max_response_per_file', default = 200, type = int)

    return parser

def codex_helper(example, prompt, idx, args, method, question, depth = 0, max_recursion = 5):
    code = get_codex_response(example + prompt)
    res = extract_ans(idx, prompt + code, method, args.task, question)
    ## bad generation, regenerate
    if (res == 'failed' or 'there' in res or res == '' or res == ' ') and depth < max_recursion:
        print(f'bad generation in {method}, regenerate: {res}')
        res = codex_helper(example, prompt, idx, args, method, question, depth = depth + 1, max_recursion = max_recursion)
    print("res: ", res)
    return res

def gpt_helper(example, prompt, idx, args, method, question, depth = 0, max_recursion = 5):
    code = get_gpt3_response(example + prompt, max_tokens = 2000)
    res = extract_ans(idx, prompt + code, method, args.task, question)
    ## bad generation, regenerate
    if (res == 'failed' or 'there' in res or res == '' or res == ' ') and depth < max_recursion:
        print(f'bad generation in {method}, regenerate: {res}')
        res = gpt_helper(example, prompt, idx, args, method, question, depth = depth + 1, max_recursion = max_recursion)
    print("res: ", res)
    return res

if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    if args.world_tracker_mode == 'all':
        args.world_tracker_mode  = ['GPT3', 'Codex_raw', 'Codex_comment', 'Codex_command', 'Codex_symbolic', 'GPT_comment', 'GPT_command', 'GPT_symbolic']

    ## Get responses
    if args.track:
        for filename in os.listdir(args.input_dir):
            task_num = filename.split("_")[0].lstrip('qa')
            if 'test' in filename and task_num in args.task:
                input_txt_path = os.path.join(args.input_dir, filename)
                output_json_path = os.path.join(args.output_dir, f"results_task_{args.task}.json")
                print(input_txt_path, output_json_path)
                
                with open(input_txt_path, 'r') as f:
                    for idx, line in enumerate(f):
                        if idx > args.max_response_per_file:
                            continue
                        print(idx)
                        dic = json.loads(line)

                        if 'GPT3' in args.world_tracker_mode:
                            prompt = gpt3_example + '\n' + dic['story'] + '\nQuestion: ' + dic['question'] + '\nAnswer:'
                            res = get_gpt3_response(prompt)
                            dic['GPT3'] = res
                        
                        if 'Codex_raw' in args.world_tracker_mode:
                            prompt = gpt3_example + '\n' + dic['story'] + '\nQuestion: ' + dic['question'] + '\nAnswer:'
                            res = get_codex_response(prompt)
                            dic['Codex_raw'] = res.strip()
                        
                        if 'Codex_comment' in args.world_tracker_mode:
                            prompt = convert_to_comment(dic['story'] + '\n' + dic['question']) + get_babi_init(args.task)
                            example = prompt_dic[args.task]['Codex_comment']
                            dic['Codex_comment'] = codex_helper(example, prompt, idx, args, 'Codex_comment', dic['question'])
                            
                        if 'Codex_command' in args.world_tracker_mode:
                            prompt = convert_to_comment(dic['story'] + '\n' + dic['question']) + get_babi_init(args.task)
                            example = prompt_dic[args.task]['Codex_command']
                            dic['Codex_command'] = codex_helper(example, prompt, idx, args, 'Codex_command', dic['question'])
                                
                        if 'Codex_symbolic' in args.world_tracker_mode:
                            prompt = convert_to_comment(dic['story'] + '\n' + dic['question']) + get_babi_init(args.task)
                            example = prompt_dic[args.task]['Codex_symbolic']
                            dic['Codex_symbolic'] = codex_helper(example, prompt, idx, args, 'Codex_symbolic', dic['question'])
                                
                        if 'GPT_comment' in args.world_tracker_mode:
                            prompt = convert_to_comment(dic['story'] + '\n' + dic['question']) + get_babi_init(args.task)
                            example = prompt_dic[args.task]['Codex_comment']
                            dic['GPT_comment'] = gpt_helper(example, prompt, idx, args, 'Codex_comment', dic['question'])
                            
                        if 'GPT_command' in args.world_tracker_mode:
                            prompt = convert_to_comment(dic['story'] + '\n' + dic['question']) + get_babi_init(args.task)
                            example = prompt_dic[args.task]['Codex_command']
                            dic['GPT_command'] = gpt_helper(example, prompt, idx, args, 'Codex_command', dic['question'])
                                
                        if 'GPT_symbolic' in args.world_tracker_mode:
                            prompt = convert_to_comment(dic['story'] + '\n' + dic['question']) + get_babi_init(args.task)
                            example = prompt_dic[args.task]['Codex_symbolic']
                            dic['GPT_symbolic'] = gpt_helper(example, prompt, idx, args, 'Codex_symbolic', dic['question'])
                        
                        print(dic)
                        dump_to_json(dic, output_json_path)
                        
    ## Get accuracy
    if args.check:
        for filename in os.listdir(args.input_dir):
            task_num = filename.split("_")[0].lstrip('qa')
            if 'test' in filename and task_num in args.task:
                output_json_path = os.path.join(args.output_dir, f"results_task_{args.task}.json")
                print("Start loading json")
                # df = pd.read_json(output_json_path, lines=True).replace('', np.nan)
                df = pd.read_json(output_json_path, lines=True).replace('', np.nan)
                print("json loaded")
                for mode in df.columns.values.tolist():
                    if mode == 'story' or mode == 'question':
                        continue
                    # mode_df = df[df[mode].notna()]
                    # df[mode + '_acc'] = mode_df[['ans', mode]].apply(lambda x: check_ans(*x), axis=1)
                    # acc = df[mode + '_acc'].dropna().mean()
                    
                    mode_df = df[df[mode]]
                    df[mode + '_acc'] = mode_df[['ans', mode]].apply(lambda x: check_ans(*x), axis=1)
                    acc = df[mode + '_acc'].mean()
                    
                    print(f"task: {args.task} mode: {mode} acc is {acc}")
                    with open("./babi_all_results.txt", 'a') as f:
                        f.write(f"task: {args.task} mode: {mode} acc is {acc}")