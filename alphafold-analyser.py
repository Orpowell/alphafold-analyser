#!/usr/bin/python3

# Import all relevant libraries
import argparse
import pickle
import sys
import matplotlib.pyplot as plt
import os


# Function to produce a PAE plot from the result_model_2_ptm.pkl file produced by AlphaFold - N.B code taken from AlphaFold CoLab
def pae_plotter(pickle_input, output):
    # Load as a dictionary from pickle file
    try:
        print('Accessing predicted alignment error data...')
        data = open(pickle_input, 'rb')
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

    # Output file for the plot
    pae_output = f'{output}/pae.png'

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
def protein_painter(pdb_input, output):
    # File path for the PyMol session
    session_path = f'{output}/pLDDT.pse'

    # Terminal Command to open pdb file, color protein by pLDDT (b-factor) and save the session in the output directory
    pymol_command = f'/Applications/PyMOL.app/Contents/MacOS/PyMOL -cq {str(pdb_input)} -d "spectrum b, yellow_green_blue; save {session_path}"'

    # Run terminal command
    os.system(pymol_command)


# Function to collect the directory storing the results from AlphaFold
def get_input():
    input_path = input('Input Directory: ')  # Receive directory storing AlphaFold results

    path = os.path.isdir(input_path)  # Check directory exists

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
    path = os.path.isdir(output_path)  # Check directory exists

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


# Argparse set-up

analyser = argparse.ArgumentParser(description='Copy file from input to output')

# Get pdb structure path
analyser.add_argument('pdb',
                      metavar='pdb_structure',
                      type=str,
                      action='store',
                      help='Path to pdb file'
                      )

# Get pkl file path
analyser.add_argument('pkl',
                      metavar='pickle_file',
                      type=str,
                      action='store',
                      help='Path to pkl file'
                      )

# Get output directory
analyser.add_argument('output',
                      metavar='output_directory',
                      type=str,
                      action='store',
                      help='Directory to store outputs'
                      )

# Parse arguments
args = analyser.parse_args()

# Assign each argument to a variable
pdb_path = args.pdb
pkl_path = args.pkl
output_directory = args.output

# Run analysis
if __name__ == '__main__':
    print(pdb_path)
    print(pkl_path)
    print(output_directory)

    pae_plotter(pkl_path, output_directory)  # Generate a PAE plot
    protein_painter(pdb_path, output_directory)  # Create a PyMol Session
