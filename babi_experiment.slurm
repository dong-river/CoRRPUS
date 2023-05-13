#!/bin/bash
#
#SBATCH --partition=p_nlp
#SBATCH --job-name=BABI
#SBATCH --output=%x.%j.log
#SBATCH --mem=16G
#SBATCH --time=36:00:00

source /home1/r/riverd/miniconda3/etc/profile.d/conda.sh
conda activate re3
cd /home1/r/riverd/world_model


python babi_experiment_new.py --track --task 2 -t GPT_comment
python babi_experiment_new.py --track --task 2 -t GPT_symbolic

python babi_experiment_new.py --check --task 2 -t GPT_comment
python babi_experiment_new.py --check --task 2 -t GPT_symbolic

# python babi_experiment_new.py --track --task 1
# python babi_experiment_new.py --track --task 3
# python babi_experiment_new.py --track --task 6
# python babi_experiment_new.py --track --task 7
# python babi_experiment_new.py --track --task 8
# python babi_experiment_new.py --track --task 9
# python babi_experiment_new.py --track --task 10
# python babi_experiment_new.py --track --task 11
# python babi_experiment_new.py --track --task 12
# python babi_experiment_new.py --track --task 13

# python babi_experiment_new.py --check --task 1
# python babi_experiment_new.py --check --task 3
# python babi_experiment_new.py --check --task 6
# python babi_experiment_new.py --check --task 7
# python babi_experiment_new.py --check --task 8
# python babi_experiment_new.py --check --task 9
# python babi_experiment_new.py --check --task 10
# python babi_experiment_new.py --check --task 11
# python babi_experiment_new.py --check --task 12
# python babi_experiment_new.py --check --task 13