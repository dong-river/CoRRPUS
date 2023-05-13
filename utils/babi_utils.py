import os
import numpy as np
from utils.babi_prompts import babi_init, babi_init_task_3
from utils.other_utils import get_codex_response, get_gpt3_response

def add_time(text):
    sents = text.strip().split('\n')
    for idx, sent in enumerate(sents):
        sents[idx] = f"at t={idx}, " + sent
    res = '\n'.join(sents) + '\n'   
    return res

def convert_to_comment(text):
    sents = text.split('\n')
    res = []
    for idx, sent in enumerate(sents):
        if sent != '':
            res.append(f"## {sent}")
    res = '\n'.join(res) + '\n'
    return res

def extract_ans(idx, code, prompt_method, task_idx, question):
    if not os.path.exists(f"./babi/codex/{prompt_method}_task_{task_idx}"):
        os.makedirs(f"./babi/codex/{prompt_method}_task_{task_idx}")
    codex_output_path = f"./babi/codex/{prompt_method}_task_{task_idx}/{idx}.py"
    print(codex_output_path)
    
    if os.path.exists(codex_output_path):
        os.remove(codex_output_path)
    with open(codex_output_path, "w") as f:
        f.write(code + '\n' + "world = World()\nworld.story()")
    try:
        ans = os.popen(f"python {codex_output_path}").read().strip()
        if task_idx == "3":
            example = "football's location history:  ['bathroom', 'garden']\nQuestion: Where is the football before garden?\nAnswer: bathroom\n===\n"
            ans = get_gpt3_response(example + ans + "\n" + "Question: " +  question)
            ans = ans.split("Answer: ")[1].strip()
    except:
        print(f"Error in running in {codex_output_path}")
        ans = 'failed'
    return ans
    
def regenerate_codex(idx, prompt):
    code = get_codex_response(prompt, temperature=0.7)
    res = extract_ans(idx, babi_init + code)
    return res

def check_ans(ans, res):
    # if len(res.split(' ')) > 10:
    #     return np.nan
    ans = ans.strip().lower()
    res = res.strip().lower()
    if 'false' in res:
        res = 'no'
    
    if "therefore" in res.lower():
        res = res.lower().split("therefore")[1]
    if ans in res:
        return True
    else:
        return False

def get_babi_init(task):
    if task == '2':
        return babi_init
    elif task == '3':
        return babi_init_task_3