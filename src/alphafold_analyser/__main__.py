import argparse
import os
import sys

from .plot_plddt import plot_pLDDT
from .paint_protein import protein_painter
from .plot_pae import plot_PAE
from .utils import *
from .__init__ import __version__

def main():
    parser = argparse.ArgumentParser(
        prog="AlphaFold Analyser",
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    group_inputs = parser.add_argument_group("Inputs")
    
    # Get pdb structure path
    group_inputs.add_argument(
        "-p",
        "--pdb",
        metavar="\b",
        type=lambda x: is_valid_file(parser, x),
        action="store",
        help="path to pdb file - generates pLDDT coloured structure",
        default=None
    )
    
    # Get pkl file path
    group_inputs.add_argument(
        "-l",
        "--pkl",
        metavar="\b",
        type=lambda x: is_valid_file(parser, x),
        action="store",
        help="path to pkl file - generates predicted aligned error plot",
        default=None,
    )

    # Get pkl file path
    group_inputs.add_argument(
        "-b",
        "--binary",
        metavar="\b",
        type=str,
        action="store",
        help="path to pymol binary - Only required for analysing pdb (-p)",
        default=None,
    )

    group_output = parser.add_argument_group("Outputs")
    
    # Get output directory
    group_output.add_argument(
        "-o",
        "--output",
        metavar="\b",
        type=str,
        action="store",
        help="directory to store all generated outputs",
        default="analyser_output",
    )

    group_options = parser.add_argument_group("Options")
    
    # Get Version
    group_options.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} v{__version__}"
    )
    
    # Get help
    group_options.add_argument(
        "-h", "--help", action="help", help="show this help message and exit\n "
    )

    # Parse arguments
    args = parser.parse_args()
    input_list = [args.pkl, args.pdb, args.output]

    # If all arguments are None display help text by parsing help
    
    if (args.pkl is None) and (args.pdb is None):
        parser.parse_args(["-h"])

    # Check output directory exists
    if not os.path.exists(args.output):
        try:
            os.makedirs(args.output)
            print(f"\nCreated output directory: {args.output}")
        except Exception as e:
            print(f"\nERROR: failed to create output directory {args.output}: {str(e)}")
            sys.exit(1)
    else:
        print(f"\nOutput directory: {args.output}")
    
    #Check binary provided if pymol file is provided
    if args.pdb is not None and args.binary is None:
        parser.error("\nERROR: pymol binary required to analyse protein structure.")

    if args.pdb is not None:
        print("\nVisualising pLDDT data...")
        protein_painter(args.pdb, args.output, args.binary)

    elif args.pdb is None:
        print("\nNo pdb file provided, skipping pLDDT data visualisation...")

    if args.pkl is not None:
        print("\nPlotting predicted aligned error and plddt...")
        plot_PAE(args.pkl, args.output)
        plot_pLDDT(args.pkl, args.output)
        
    elif args.pkl is None:
        print(
            "\nNo pickle file provided, skipping predicted aligned error visualisation..."
        )
        
    print("\nAll processes finished, shutting down.")


if __name__ == "__main__":
    main()
    sys.exit(0)