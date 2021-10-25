#!/usr/bin/python3

# Import all relevant libraries
import pickle
import sys
import matplotlib.pyplot as plt
import os


# Function to produce a PAE plot from the result_model_2_ptm.pkl file produced by AlphaFold - N.B code taken from AlphaFold CoLab
def pae_plotter():
    pae_path = f'{input_directory}/result_model_2_ptm.pkl'  # File containing data
    pae_output = f'{result_dir}/{protein}-pae.png'  # Output file for the plot

    # Load as a dictionary from pickle file
    try:
        print('Accessing predicted alignment error data...')
        data = open(pae_path, 'rb')
        prediction_result = pickle.load(data)
        data.close()

    # If the file does not exist, the program will exit.
    except FileNotFoundError:
        print('Error: result_model_2_ptm.pkl could not be found input directory.')
        sys.exit()

    # Generate dictionary for predicted aligned error results from pkl file
    print('Processing predicted alignment error data...')
    pae_outputs = {'protein': (
        prediction_result['predicted_aligned_error'],
        prediction_result['max_predicted_aligned_error']
    )}

    # Plot predicted align error results for each aligned residue
    print('Plotting predicted alignment error data...')
    pae, max_pae = list(pae_outputs.values())[0]
    fig = plt.figure()  # generate figure
    fig.set_facecolor('white')  # color background white
    plt.imshow(pae, vmin=0., vmax=max_pae)  # plot pae
    plt.colorbar(fraction=0.46, pad=0.04)  # create color bar
    plt.title('Predicted Aligned Error')  # plot title
    plt.xlabel('Scored residue')  # plot x-axis label
    plt.ylabel('Aligned residue')  # plot y-axis label

    plt.savefig(pae_output, dpi=1000, bbox_inches='tight')  # save plot to output directory
    print('Task complete')


# Function to create a PyMOL session from the ranked_0.pdb file produced by AlphaFold
def protein_painter():
    # Set file paths to access pdb structure and save output pymol session
    check_structure_path = f'{input_directory}/ranked_0.pdb'    # File path to access the pdb structure
    session_path = f'{result_dir}/{protein}.pse'    # File path for the PyMol session
    path = os.path.isfile(check_structure_path)   # Check the Output Directory exists
    structure_path = f'"{input_directory}/ranked_0.pdb"'        # File formatted for PyMol
    # Checks file exists and creates a pymol session
    if path is True:
        # Terminal Command to open pdb file, color protein by pLDDT (b-factor) and save the session in the output directory
        pymol_command = f'/Applications/PyMOL.app/Contents/MacOS/PyMOL -cq {str(structure_path)} -d "spectrum b, yellow_green_blue; save {session_path}"'

        # Run terminal command
        os.system(pymol_command)

    # If the file doesn't exist, the program will exited.
    else:
        print('Error: ranked_0.pdb not found in input directory.')
        sys.exit()


# Function to collect the directory storing the results from AlphaFold
def get_input():
    input_path = input('Input Directory: ')     # Receive directory storing AlphaFold results

    path = os.path.isdir(input_path)    # Check directory exists

    # If directory exists return directory
    if path is True:
        print('Input directory accepted')
        return input_path

    # If directory doesn't exist, ask again
    else:
        print('Error directory not found. Please use an existing directory.')
        path = get_input()
        return path


# Function to create file paths and directories to store analysis outputs
def get_output():
    output_path = input('Output Directory: ')  # Input File path for directory containing results
    protein_label = input('Protein: ')  # Input the name of the protein - used to label directories and files
    path = os.path.isdir(output_path)   # Check directory exists

    # If the directory exists generate output directory and return all relevant variables
    if path is True:
        print('Input directory accepted')

        result_path = f'{output_path}/{protein_label}'  # Generate directory to store results

        # Check directory doesn't already exist
        try:
            os.mkdir(result_path)

        except FileExistsError:
            print(f'Results will stored in: {result_path}')
            pass

        return output_path, result_path, protein_label

    # If directory doesn't exist, ask again
    else:
        print('Error output directory not found. Please use an existing directory.')
        path = get_output()
        return path


# Run analysis
if __name__ == '__main__':
    input_directory = get_input()  # Input File path for directory containing AlphaFold results
    output_directory, result_dir, protein = get_output()  # Input File path for directory containing results
    pae_plotter()   # Generate a PAE plot
    protein_painter()   # Create a PyMol Session

# /Users/oliverpowell/OneDrive - Norwich BioScience Institutes/alphafold/data/predictions/yeast-erg24-mutants/yeast-erg24-V290L
# /Users/oliverpowell/OneDrive - Norwich BioScience Institutes/alphafold/analysis/yeast-erg24-mutants/
# yeast-erg24-D286N