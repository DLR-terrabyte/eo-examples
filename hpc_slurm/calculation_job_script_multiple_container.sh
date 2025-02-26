#!/bin/bash

#SBATCH -J simple_calculation
#SBATCH -o calculation.%a.out
#SBATCH -e calculation.%a.err
#SBATCH -D .
#SBATCH --clusters=hpda2
#SBATCH --partition=hpda2_compute
#SBATCH --cpus-per-task=1
#SBATCH --mem=1gb
#SBATCH --time=00:05:00
#SBATCH --mail-type=all
#SBATCH --mail-user=<your.adress@mail.de>
#SBATCH --account=hpda-c
#SBATCH --array=1-10

module load slurm_setup
module use /dss/dsstbyfs01/pn56su/pn56su-dss-0020/usr/share/modules/files/
module load charliecloud/0.39

ch-run python.sqfs --home -b /dss/.:/dss/ -- python ~/eo-examples/hpc_slurm/calculation.py $SLURM_ARRAY_TASK_ID

