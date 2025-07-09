import os
import pickle
import json
from .__init__ import __version__

# Output Multimer specific stats if present
def multimer_stats(data):
    ptm = data["ptm"]
    iptm = data["iptm"]
    # [0.8 ipTM + 0.2 pTM] from Homma et al. 2023
    # Ratio > 0.75 is considered a good prediction of interaction
    ratio = (0.8 * iptm) + (0.2 * ptm)
    print("\n#### Multimer Stats ####")
    print(f"pTM: {ptm:.3f}")
    print(f"ipTM: {iptm:.3f}")
    print(f"[0.8 ipTM + 0.2 pTM]: {ratio:.3f}")
    
# Checks if a file exists
def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error(f"Input file ({arg}) not found!")

    else:
        return arg

# Unpickle file and return dictionary
def depickler(pickle_input):
    try:
        with open(pickle_input, "rb") as f:
            return pickle.load(f)

    except EOFError:
        print(
            "\nERROR: Data could not be found, predicted aligned error plotting failed."
        )

def load_json(input):
    try:
        with open(input, "rb") as f:
            return json.load(f)
    
    except EOFError:
        print(
            "\nERROR: Data could not be found, predicted aligned error plotting failed."
        )

def splash(args) -> None:
    
    command = None
    
    print(f"""
############################
# AlphaFold-Analyser v{__version__}#
############################""")
    
    for k, v in vars(args).items():
        
        if k == 'command':
            command = v

        if k == "plot_contacts" and (command != 'pae'):
            continue
        
        if k == "alphafold3" and (command == 'structure'):
            continue
    
        print(f"{k}: {v}")