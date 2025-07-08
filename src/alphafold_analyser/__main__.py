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
        help="path to PKL file",
        required=False,
        default=None
    )

    common_inputs_parser.add_argument(
        "-j",
        "--json",
        metavar="\b",
        type=lambda x: is_valid_file(parser, x),
        action="store",
        help="path to JSON file",
        required=False,
        default=None
    )
    
    common_inputs_parser.add_argument(
        "-af3",
        "--alphafold3",
        action="store_true",
        help="Analyse AlphaFold3 data (json)",
        required=False,
    )
    
    plddt_parser = sub_parsers.add_parser("plddt", parents=[common_inputs_parser])
    
    plddt_parser.add_argument(
        "-o",
        "--output",
        metavar="\b",
        type=str,
        action="store",
        help="Predicted aligned error (PAE) plot [*.svg, *.png]",
        default="plddt.png"
    )
    
    pae_parser = sub_parsers.add_parser("pae", parents=[common_inputs_parser])
    
    pae_parser.add_argument(
        "-o",
        "--output",
        metavar="\b",
        type=str,
        action="store",
        help="Predicted aligned error (PAE) plot [*.svg, *.png]",
        default="PAE.png"
    )
    
    structure_parser = sub_parsers.add_parser("structure", parents=[common_inputs_parser])
    
    structure_parser.add_argument(
        "-s",
        "--structure",
        metavar="\b",
        type=lambda x: is_valid_file(parser, x),
        action="store",
        help="path to protein structure file [*.pdb, *.cif]",
        required=True
    )
    
    structure_parser.add_argument(
        "-b",
        "--binary",
        metavar="\b",
        type=str,
        action="store",
        help="path to pymol binary",
        required=True
    )
    
    structure_parser.add_argument(
        "-o",
        "--output",
        metavar="\b",
        type=str,
        action="store",
        help="Pymol session",
        default="protein.pse"
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # If all arguments are None display help text by parsing help
    if (args.pkl is None) and (args.json is None):
        parser.parse_args(["-h"])
        
    if (args.pkl is not None) and (args.json is not None):
        print("\nCan't parse json and pkl data at the same time!")
        parser.parse_args(["-h"])
    
    if args.command == "plddt":
        print("\nPlotting plddt...")
        plot_pLDDT(args.pkl, args.output, args.alphafold3)
        
    
    if args.command == 'pae':
        print("\nPlotting predicted aligned error...")
        plot_PAE(args.pkl, args.output, args.alphafold3) 
        
    
    if args.command == 'structure':
        print("\nVisualising pLDDT data...")
        protein_painter(args.structure, args.output, args.binary, args.alphafold3)
    
    sys.exit(0)

    


if __name__ == "__main__":
    main()
   