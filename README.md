# CoRRPUS
This repo is the implementation for our [paper](https://arxiv.org/abs/2212.10754):

```
 @inproceedings{Dong2023CoRRPUS, 
 address={Toronto, Canada}, 
 title={{CoRRPUS: Code-based Structured Prompting for Neurosymbolic Story Understanding}}, 
 url={http://arxiv.org/abs/2212.10754}, 
 booktitle={Findings of the Association for Computational Linguistics: ACL 2023}, 
 author={Dong, Yijiang River and Martin, Lara J. and Callison-Burch, Chris}, 
 year={2023}, 
 month={Jul}, 
 publisher={Association for Computational Linguistics}
 }
```

### Preparation
First install the dependencies by running the following command.
```
conda create -n corrpus python=3.8
conda activate corrpus
pip install -r requirements.txt
```

And then you need to provide your OpenAI Key by running 
```
export OPENAI_API_KEY=YOUR_KEY
```

### Experiments on bAbI

To reproduce our experiments on bAbI. You should run the following command where -t controls the model (world tracker) used.
```
python babi_experiment.py --track --check -t Codex_comment
```
Other world trackers include GPT3, Codex_raw, Codex_comment, Codex_command, Codex_symbolic, GPT_comment, GPT_command, GPT_symbolic. 
You can also pass in "all" to run all the experiments
```
python babi_experiment.py --track --check -t all
```
Then the code will be generated in `./babi/codex/Codex_comment_task_2` and the result after executing the code is shown in `./babi/codex/results_task_2.json`. The final accuracy will in shown in `babi_all_results.txt`.

### Experiments on $Re^3$

Similarly, to reproduce our experiments on $Re^3$, you should run the following command where -t controls the model (world tracker) used.

```
python re3_experiments.py --track --check -t Codex_comment
python re3_experiments.py --track --check -t Codex_abstract
python re3_experiments.py --track --check -t Codex_function
```
Then the code will be generated in `./re3_exp/Codex_abstract/story_4/consistent_1_0_story.py` (for example).

The final AUC will be written in `./re3_exp/Codex_function/TE_log.txt`.
