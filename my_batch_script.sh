#!/bin/bash
  
#SBATCH --partition=debug
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=1
#SBATCH --time=00:05
#SBATCH --job-name "hello world!"
#SBATCH --output %j_%x.out


srun echo "Hello"

srun echo $SLURM_JOB_NODELIST
srun echo $SLURM_JOB_CPUS_PER_NODE

srun sleep 10

srun echo "World!"
