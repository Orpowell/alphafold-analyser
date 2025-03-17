#!/usr/bin/env bash
#SBATCH -J alphafold
#SBATCH --partition=gpu
#SBATCH --gpus=1
#SBATCH --cpus-per-gpu=2
#SBATCH --mem-per-gpu=8G

# INPUT
Pickle=$1
PDB=$2
OutDir=$3

# ENVIRONMENT VARIABLES
AppDir=/mnt/apps/users/jnprice/alphafold-analyser
PymolBin=/mnt/apps/users/jnprice/conda/envs/alphafold_vis/bin/pymol

# ACTIVATE CONDA ENVIRONMENT
source activate alphafold-analyser

# CHECK FOR INPUTS
if [[ -f $Pickle && -f $PDB && -n $OutDir ]]; then
    # CREATE OUTPUT FOLDER IF IT DOESN'T EXIST
    if [[ ! -d $OutDir ]]; then
        mkdir -p "$OutDir"
    fi

    # RUN ANALYSER
    python $AppDir/alphafold-analyser.py \
        --pkl $Pickle \
        --pdb $PDB \
        --binary $PymolBin \
        --output $OutDir

else
    # PRINT ERROR & USAGE MESSAGES
    echo -e "\nERROR: Expected inputs not found. Please provide Pickle and PDB files for the same prediction and an output directory. \n"
    echo -e "Usage: sbatch alphafold_analyser_submit.sh <pickle_file> <pdb_file> <output_directory> \n"
    exit 1
fi

