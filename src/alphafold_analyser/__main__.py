import argparse
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
        "-d",
        "--data",
        metavar="\b",
        type=lambda x: is_valid_file(parser, x),
        action="store",
        help="path to prediciton data: *.pkl (AF2) or *.json (AF3)",
        required=False,
        default=None
    )
    
    plddt_parser = sub_parsers.add_parser("plddt", parents=[common_inputs_parser])
    
    plddt_parser.add_argument(
        "-o",
        "--output",
        metavar="\b",
        type=str,
        action="store",
        help="Predicted aligned error (PAE) plot [*.png]",
        default="plddt.png"
    )
    
    plddt_parser.add_argument(
        "-af3",
        "--alphafold3",
        action="store_true",
        help="Analyse AlphaFold3 data (json)",
        required=False,
    )
    
    pae_parser = sub_parsers.add_parser("pae", parents=[common_inputs_parser])
    
    pae_parser.add_argument(
        "-af3",
        "--alphafold3",
        action="store_true",
        help="Analyse AlphaFold3 data (json)",
        required=False
    )
    
    pae_parser.add_argument(
        "-pc",
        "--plot_contacts",
        action="store_true",
        help="Plot contact data instead of predicted aligned error",
        required=False,
    )
    
    pae_parser.add_argument(
        "-o",
        "--output",
        metavar="\b",
        type=str,
        action="store",
        help="Predicted aligned error (PAE) plot [*.png]",
        default="PAE.png"
    )
    
    structure_parser = sub_parsers.add_parser("structure")
    
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
    args = parser.parse_args(sys.argv[1:] or ['--help'])
    splash(args)

    if args.command == 'structure':
        print("\nVisualising pLDDT data...")
        protein_painter(args.structure, args.output, args.binary)
        print("Task complete...")
        sys.exit(0)
    
    if args.command == "plddt":
        print("\nPlotting plddt...")
        plot_pLDDT(args.data, args.output, args.alphafold3)
        print("Task complete...")
        sys.exit(0)
    
    if args.command == 'pae':
        
        if (args.plot_contacts is True) and (args.alphafold3 is False):
            print("\nContacts can only be plotted for AlphaFold3 predictions!")
            parser.parse_args(["-h"])
            sys.exit(1)
        
        if args.plot_contacts:
            print("\nPlotting contacts...")
        
        if args.plot_contacts is False:
            print("\nPlotting predicted aligned error...")
        
        plot_PAE(args.data, args.output, args.alphafold3, args.plot_contacts)
        
        print("Task complete...")
        
        sys.exit(0)


if __name__ == "__main__":
    main()
   