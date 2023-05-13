#!/bin/bash
#
#SBATCH --partition=p_nlp
#SBATCH --job-name=RE3
#SBATCH --output=%x.%j.log
#SBATCH --mem=16G
#SBATCH --nodelist=nlpgpu03
#SBATCH --gpus=1
#SBATCH --time=24:00:00

source /home1/r/riverd/miniconda3/etc/profile.d/conda.sh
conda activate re3
cd /home1/r/riverd/world_model
python re3_experiments.py --track