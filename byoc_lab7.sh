#!/bin/bash
  
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00
#SBATCH --job-name=segy_plot
#SBATCH --output=%j.out

# I resorted to using AI to figure out how to activate the environment
source ~/miniforge3/etc/profile.d/conda.sh
conda activate GEOS694

INPUT_SEGY="~cnsmith13/he0703_2007_229_1847_LF_000.sgy"
OUTPUT_PNG="segy_plot.png"

python lab7_byoc_smith.py $INPUT_SEGY $OUTPUT_PNG