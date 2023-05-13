# CoRRPUS
This repo is the implementation for our [paper](https://arxiv.org/pdf/2212.10754.pdf):

"CORRPUS: Codex-Leveraged Structured Representations for Neurosymbolic Story Understanding"
Yijiang River Dong, Lara J. Martin, and Chris Callison-Burch. Findings of ACL 2023.

### Preparation
First install the dependencies by running the following command.
```
conda create -n corrpus python=3.8
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
