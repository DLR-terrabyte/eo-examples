#!/bin/bash

#SBATCH -J simple_calculation
#SBATCH -o calculation.out
#SBATCH -e calculation.err
#SBATCH -D .
#SBATCH --clusters=hpda2
#SBATCH --partition=hpda2_compute
#SBATCH --cpus-per-task=1
#SBATCH --mem=1gb
#SBATCH --time=00:05:00
#SBATCH --mail-type=all
#SBATCH --mail-user=<your.adress@mail.de>
#SBATCH --account=hpda-c

module load slurm_setup
module load python

python calculation.py 5

