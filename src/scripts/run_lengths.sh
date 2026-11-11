#!/bin/bash -l
#SBATCH --job-name=lengths
#SBATCH --output=logs/%x_%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=mit_normal
#SBATCH --mem=16G
#SBATCH --time=06:00:00
#SBATCH --array=0-6

# Submit from src/scripts:  sbatch run_lengths.sh
# One array task per language; lengths.py is single-threaded.
LANGS=(de en es it ja nl ta)
LANG_ID=${LANGS[$SLURM_ARRAY_TASK_ID]}

set -euo pipefail
cd "$HOME/prosody/Prosody_Project"
source .venv/bin/activate
cd src

echo "Started $LANG_ID $(date) on $(hostname)"
PYTHONPATH=. python scripts/lengths.py "$LANG_ID"
echo "Finished $LANG_ID $(date)"
