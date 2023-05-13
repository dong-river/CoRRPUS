import os
import re
import copy
import string
from utils.prompts import *
from utils.other_utils import split_into_sentences, text_to_code, get_gpt3_response, get_codex_response, write_to_file


def create_character_prompt(info):
    character_names = info['character_strings'].keys()
    character_prompt = """class World:
    def __init__(self):
"""
    for character_name in character_names:
        character_prompt += f"        self.{character_name.replace(' ', '_')} = character('{character_name}')\n"
    character_prompt += '\n'
    return character_prompt

def create_story_prompt(text, header, include_first_line_of_function = True):
    if header == "story_setting":
        story_prompt = """
    def story_setting(self):
"""
    elif header == "story":
        story_prompt = """
    # For all functions in this section, check for consistency
    def story(self):
"""
    else:
        print('wrong header')
        raise NotImplementedError
    
    sents = split_into_sentences(text.strip('\n'))
    code_lines = [text_to_code(sent) for sent in sents]
    for code_line in code_lines:
        story_prompt += "        " + "self." + code_line + "\n"
    first_function_prompt = f"\n    def {code_lines[0]}(self):\n"
    
    if include_first_line_of_function:
        return story_prompt + first_function_prompt
    return story_prompt

def event_extraction(story, characters):
    chars = ", ".join(characters)
    instruction = f"Parse the following story into simple events about {chars}"
    res = get_codex_response(instruction + '\n' + story + '\n\nEvents:')
    return res

def get_world_model(file_path, subsubfolder):
    folder_path, subfolder_name, story_idx = subsubfolder.split('/')[-3], subsubfolder.split('/')[-2], subsubfolder.split('/')[-1]
    exec(f"from {folder_path}.{subfolder_name}.{story_idx}.{file_path.replace('.py', '')} import World", globals())
    world = World()
    return world

def tracker_codex_abstract(info, story, setting_or_story, sub_folder, subsubfolder, output_path, trail_count=0, max_trails=5):
    if setting_or_story == 'story_setting':
        sents = split_into_sentences(info['infer_attributes_string'])
    elif setting_or_story == 'story':
        sents = split_into_sentences(story)
    example = codex_function_abstract_example
    character_prompt = create_character_prompt(info)
        
    instruction = ""
    for sent in sents:
        instruction += f"## {sent}\n"
    instruction += "\n## Create a world model state to track each character's appearance, personality, and relations with other characters.\n"
    prompt = instruction + codex_init_prompt_3 + character_prompt +  function_definition_example + f"    def story(self):\n"
    res = get_codex_response(example + prompt)
    output = prompt + res
    write_to_file(output, sub_folder, subsubfolder, output_path)
    
    if check_bad_generation(output, output_path):
        if trail_count < max_trails:
            return tracker_codex_comment(info, story, setting_or_story, sub_folder, subsubfolder, output_path, trail_count + 1, max_trails)
        else:
            return output
    return output

def tracker_codex_comment(info, story, setting_or_story, sub_folder, subsubfolder, output_path, trail_count=0, max_trails=5):
    if setting_or_story == 'story_setting':
        sents = split_into_sentences(info['infer_attributes_string'])
    elif setting_or_story == 'story':
        sents = split_into_sentences(story)
    example = codex_comment_example
    character_prompt = create_character_prompt(info)
        
    instruction = ""
    for sent in sents:
        instruction += f"## {sent}\n"
    instruction += "## Create a world model state to track each character's appearance, personality, and relations with other characters.\n"
    prompt = instruction + codex_init_prompt_3 + character_prompt + f"    def story(self):\n"
    res = get_codex_response(example + prompt)
    output = prompt + res
    write_to_file(output, sub_folder, subsubfolder, output_path)
    
    if check_bad_generation(output, output_path):
        if trail_count < max_trails:
            return tracker_codex_comment(info, story, setting_or_story, sub_folder, subsubfolder, output_path, trail_count + 1, max_trails)
        else:
            return output
    return output

def tracker_codex_function(info, story, setting_or_story, sub_folder, subsubfolder, output_path, trail_count=0, max_trails=5):
    instruction = "## Create a world model state to track each character's appearance, personality, and relations with other characters.\n"
    if setting_or_story == 'story_setting':
        sents = split_into_sentences(info['infer_attributes_string'])
    elif setting_or_story == 'story':
        sents = split_into_sentences(story)
    example = codex_function_example
    character_prompt = create_character_prompt(info)
        
    sents = '\n'.join(['        self.' + text_to_code(sent) + '()' for sent in sents])
    prompt = instruction + codex_init_prompt_3 + character_prompt + f"    def story(self):\n" + sents + '\n    def'
    res = get_codex_response(example + prompt)
    output = prompt + res
    write_to_file(output, sub_folder, subsubfolder, output_path)
    
    if check_bad_generation(output, output_path):
        if trail_count < max_trails:
            return tracker_codex_function(info, story, setting_or_story, sub_folder, subsubfolder, output_path, trail_count + 1)
        else:
            return output
    return output

def check_bad_generation(generation, file_path):
    if os.path.exists(generation):
        with open(generation, 'r') as f:
            generation = f.read()
    
    ## If no dictionary update after story
    tmp = generation.split('story(self):')[-1].strip().split('\n')
    if sum([not sent.strip().startswith('##') for sent in tmp]) == False: ## all sentences start with ##
        print('bad generation: no dictionary update after story')
        return True
    
    ## If no def story(self) in the generation
    if "def story(self)" not in generation and "def story_setting(self)" not in generation:
        print("bad generation: no def story(self) in the generation")
        return True
    
    ## if appending everything
    tmp = re.findall(r"'(.*?)'", generation)
    tmp = [x for x in tmp if len(x.split(' ')) > 3]
    if len(tmp) > 5:
        print("appending everything")
        return True
    
    ## if code cannot be executed
    try:
        folder_path, subfolder_name, story_idx, file_path = file_path.split('/')[-4], file_path.split('/')[-3], file_path.split('/')[-2], file_path.split('/')[-1]
        exec(f"from {folder_path}.{subfolder_name}.{story_idx}.{file_path.replace('.py', '')} import World", globals())
        world = World()
        try: 
            world.story()
        except:
            world.story_setting()
    except:
        print("code cannot be executed")
        return True
    
    return False