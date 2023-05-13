# CoRRPUS

This repo is the implementation for our [paper](https://arxiv.org/pdf/2212.10754.pdf):

"CORRPUS: Codex-Leveraged Structured Representations for Neurosymbolic Story Understanding"
Yijiang River Dong, Lara J. Martin, and Chris Callison-Burch. Findings of ACL 2023.

### Experiments on bAbI

To reproduce our experiments on bAbI. You should run the following command where -t controls the model (world tracker) used.
```
python babi_experiment_new.py --track -t Codex_comment
```
Other world trackers include GPT3, Codex_raw, Codex_comment, Codex_command, Codex_symbolic, GPT_comment, GPT_command, GPT_symbolic. You can also pass in "all" to 
run all the experiments
```
python babi_experiment_new.py --track -t all
```
Then it will output the accuracy to `babi_all_results.txt`.

### Experiments on Re^3
