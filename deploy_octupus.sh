#!/bin/bash
#SBATCH --job-name=octupus_llm
# The line below writes to a logs dir inside the one where sbatch was called
# %x will be replaced by the job name, and %j by the job id
#SBATCH --output=logs/%x-%j.out
#SBATCH -n 1 # Number of tasks
#SBATCH --cpus-per-task 1  # number cpus (threads) per task

#SBATCH --mem=30GB # Memory - Use up to 2GB per requested CPU as a rule of thumb
# SBATCH --time=0 # No time limit

# replace the XXX with nvidia_a100-pcie-40gb or nvidia_a100-sxm4-40gb
# replace the YYY with the number of GPUs that you need, 1 to 8 PCIe or 1 to 4 SXM4
# ... --gres=gpu:XXX:YYY

# SBATCH --gres=gpu:1
# SBATCH --gres=gpu:nvidia_a100-pcie-40gb:2
# SBATCH --gres=gpu:nvidia_a100-sxm4-40gb:2
#SBATCH --gres=gpu:nvidia_a100-pcie-40gb:1

eval "$(conda shell.bash hook)"

# activate your anaconda environment
conda activate mind2nav

# change dir to where you want to run scripts
# cd /home/j.soares/twiz-opensearch/

# run program
# not working due to import errors but works in local pc
PYTHONUNBUFFERED=1 python3 experiment/octupus.py