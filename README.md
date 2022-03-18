# AlphaFold Analyser

AlphaFold Analyser is a command line tool to produce high quality visualisations of protein structures predicted by AlphaFold. These visualisations allow the user to view the pLDDT of each residue of a protein structure and the predicted alignment error for the entire protein to rapidly infer the quality of a predicted structure.

Dependencies for AlphaFold Analyser can be found in [requirements.txt](https://github.com/Orpowell/alphafold-analyser/blob/master/requirements.txt). In addition the following software is also required:
- Python >=3.7
- PyMol == 2.5.2

## Installing AlphaFold Analyser on Linux & MacOSX

At the command line, change directory to the directory where alphafold-analyser.py was downloaded, , using the full path name.

	cd <download-directory>

Now move the file to where you normally keep your binaries. This directory should be in your path. Note: you may require administrative privileges to do this (either switching user to root or by using sudo).

As root:

	mv alphafold-analyser.py /usr/local/bin/

As regular user:

	sudo mv alphafold-analyser.py /usr/local/bin/

alphafold-analyser.py should now run from the shell or Terminal using the command alphafold-analyser.py

Alternatively, alphafold-analyser.py can be run directly from an IDE.

## Using AlphaFold Analyser
GIF

When running alphafold analyser, 

All commands require an output directory to be specified (-o or —output_directory) and can be run simultaneously.  

#### Creating a pLDDT annotated structure
A pLDDT annotated structure can be generated using the following command:

	alphafold-analyser.py --pdb protein.pdb -o my_directory

#### Generating a predicted alignment error plot
A pae plot can be generated using the following command:

	alphafold-analyser.py --pkl protein.pkl -o my_directory

