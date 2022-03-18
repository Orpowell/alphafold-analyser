#!/usr/bin/python3.7

# Import all relevant libraries
import argparse
import os
import pickle
import matplotlib.pyplot as plt


# Create a PAE plot from the pkl file produced by AlphaFold - N.B code taken from AlphaFold CoLab
def pae_plotter(pickle_input, output):
    # Load as a dictionary from pickle file
    data = open(pickle_input, 'rb')
    prediction_result = pickle.load(data)
    data.close()

    # Generate dictionary for predicted aligned error results from pkl file
    pae_outputs = {'protein': (
        prediction_result['predicted_aligned_error'],
        prediction_result['max_predicted_aligned_error']
    )}

    # Output file_path for the plot
    pae_output = f'{output}/pae.png'

    # Plot predicted align error results for each aligned residue
    pae, max_pae = list(pae_outputs.values())[0]
    fig = plt.figure()  # generate figure
    fig.set_facecolor('white')  # color background white
    plt.imshow(pae, vmin=0., vmax=max_pae)  # plot pae
    plt.colorbar(fraction=0.46, pad=0.04)  # create color bar
    plt.title('Predicted Aligned Error')  # plot title
    plt.xlabel('Scored residue')  # plot x-axis label
    plt.ylabel('Aligned residue')  # plot y-axis label

    plt.savefig(pae_output, dpi=1000, bbox_inches='tight')  # save plot to output directory


# Create a PyMOL session from the pdb file generated by AlphaFold
def protein_painter(pdb_input, output):
    # File path for the PyMol session
    session_path = f'{output}/pLDDT.pse'

    # Terminal Command to open pdb file, color protein by pLDDT (b-factor) and save the session in the output directory
    pymol_command = f'PyMol -cq {str(pdb_input)} -d "spectrum b, yellow_green_blue; save {session_path}"'

    # Run terminal command
    os.system(pymol_command)


# Generate CLI and define arguments with Argparse
def cmd_lineparser():
    parser = argparse.ArgumentParser(prog='AlphaFold Analyser', exit_on_error=True, add_help=False, formatter_class=argparse.RawTextHelpFormatter)

    group_inputs = parser.add_argument_group('Inputs')
    # Get pdb structure path
    group_inputs.add_argument('-p', '--pdb', metavar='\b', type=str, action='store', help='path to pdb file - generates pLDDT coloured structure',
                              default=None)
    # Get pkl file path
    group_inputs.add_argument('-l', '--pkl', metavar='\b', type=str, action='store', help='path to pkl file - generates predicted alignment error plot',
                              default=None)

    group_output = parser.add_argument_group('Outputs')
    # Get output directory
    group_output.add_argument('-o', '--output', metavar='\b', type=str, action='store',
                              help='directory to store all generated outputs', default=None)

    group_options = parser.add_argument_group('Options')
    # Get Version
    group_options.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')
    # Get help
    group_options.add_argument("-h", "--help", action="help", help="show this help message and exit\n ")

    # Parse arguments
    args = parser.parse_args()
    input_list = [args.pkl, args.pdb, args.output]

    # If all arguments are None display help text by parsing help
    if input_list.count(input_list[0]) == len(input_list):
        parser.parse_args(['-h'])

    # Check arg.pdb input is a pdb file
    if args.pdb is not None:
        if not args.pdb.endswith('.pdb'):
            parser.error('ERROR: --pdb requires pdb file as input')

    # Check arg.pkl input is a pkl file
    if args.pkl is not None:
        if not args.pkl.endswith('.pkl'):
            parser.error('ERROR: --pkl requires pkl file as input')

    # Check output directory exists
    if not os.path.isdir(args.output):
        parser.error('ERROR: Output directory not found')

    return args


# Perform analysis of alphafold results
def main():
    args = cmd_lineparser()

    # if pdb structure provided and generates PyMol session with pLDDT coloured
    if args.pdb is not None:
        print('\n Visualising pLDDT data...\n')
        protein_painter(args.pdb, args.output)
        print('\n pLDDT data visualised\n')

    # if no pdb structure provided skips process
    elif args.pdb is None:
        print(' Skipping pLDDT data visualisation...\n')

    # if pkl structure provided, generate predicted aligned error plot
    if args.pkl is not None:
        print(' plotting predicted alignment error...\n')
        pae_plotter(args.pkl, args.output)
        print(' predicted alignment error plotted\n')

    # if no pkl file provided skips process
    elif args.pkl is None:
        print(' skipping predicted alignment error visualisation...\n')

    print(' all tasks complete, shutting down...\n')


# Run analysis
if __name__ == '__main__':
    main()
