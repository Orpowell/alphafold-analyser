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
    
    sub_parsers = parser.add_subparsers(dest="command")

    # Versioning
    parser.add_argument(
        "-v", "--version", action="version", version=f"{parser.prog} v{__version__}"
    )
    
    # Help
    parser.add_argument(
        "-h", "--help", action="help", help="show this help message and exit\n "
    )
    
    common_inputs_parser = argparse.ArgumentParser(add_help=False)
    
    common_inputs_parser.add_argument(
        "-l",
        "--pkl",
        metavar="\b",
        type=lambda x: is_valid_file(parser, x),
        action="store",
        help="path to pkl file - can generate both PAE and PLDDT plots",
        required=True
    )
    
    common_inputs_parser.add_argument(
        "-o",
        "--output",
        metavar="\b",
        type=str,
        action="store",
        help="directory to store all generated outputs",
        default="analyser_output",
    )
    
    protein_input_parser = argparse.ArgumentParser(add_help=False)
    
    protein_input_parser.add_argument(
        "-p",
        "--pdb",
        metavar="\b",
        type=lambda x: is_valid_file(parser, x),
        action="store",
        help="path to pdb file - generates pLDDT coloured structure",
        default=None
    )
    
    protein_input_parser.add_argument(
        "-b",
        "--binary",
        metavar="\b",
        type=str,
        action="store",
        help="path to pymol binary - Only required for analysing pdb (-p)",
        default=None,
    )
    
    plddt_parser = sub_parsers.add_parser("plddt", parents=[common_inputs_parser])
    pae_parser = sub_parsers.add_parser("pae", parents=[common_inputs_parser])
    structure_parser = sub_parsers.add_parser("structure", parents=[common_inputs_parser, protein_input_parser])
    
    # Parse arguments
    args = parser.parse_args()
    
    # If all arguments are None display help text by parsing help
    
    if (args.pkl is None):
        parser.parse_args(["-h"])
    
    # Check output directory exists
    if not os.path.exists(args.output):
        try:
            os.makedirs(args.output)
            
        except Exception as e:
            print(f"\nERROR: failed to create output directory {args.output}: {str(e)}")
            sys.exit(1)
    
    print(f"\nOutput directory: {args.output}")
    
    if args.command == "plddt":
        print("\nPlotting plddt...")
        plot_pLDDT(args.pkl, args.output)
    
    if args.command == 'pae':
        print("\nPlotting predicted aligned error...")
        plot_PAE(args.pkl, args.output) 
    
    if args.command == 'structure':
        print("\nVisualising pLDDT data...")
        protein_painter(args.pdb, args.output, args.binary)

    sys.exit(0)


if __name__ == "__main__":
    main()
   