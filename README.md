# AlphaFold Analyser

AlphaFold Analyser is a command line tool to produce high quality visualisations of protein structures predicted by AlphaFold2. These visualisations allow the user to view the pLDDT of each residue of a protein structure and the predicted alignment error for the entire protein to rapidly infer the quality of a predicted structure. Alphafold analyser can process the results of both multimer and monomer predictions.

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

Please note: to plot the predicted aligned error of a monomer; AlphaFold must be run using the setting —model_preset=monomer_ptm (ptm models are automatically generated for multimer predictions).

When running alphafold analyser,  please ensure the structure and pickle file used are for the same prediction. All commands require an output directory to be specified (-o or —output_directory) and can be run simultaneously.  

	alphafold-analyser.py --pkl protein.pkl --pdb protein.pdb --binary path/to/pymol/binary --output my_directory

#### Creating a pLDDT annotated structure
A pLDDT annotated structure can be generated using the following command:

	alphafold-analyser.py --pdb protein.pdb --binary path/to/pymol/binary --output my_directory

#### Generating a predicted alignment error and pLDDT  plot
A pae plot can be generated using the following command:

	alphafold-analyser.py --pkl protein.pkl --output my_directory

## Outputs

![outputs](https://github.com/Orpowell/alphafold-analyser/blob/main/img/outputs.png)

AlphaFold Analyser creates the following outputs:

1. A plot of pLDDT across the structure (plddt.png).

2. A PyMol session (pLDDT.pse): This will contain the structure predicted by AlphaFold with each individual residues coloured according to their pLDDT as follows:

	| Colour | pLDDT confidence |	
	|---|---|
	| Blue  | Very high (pLDDT > 90) |
	| Cyan 	| High (90 > pLDDT > 70) |
	| Orange | Low (70 > pLDDT > 50) |
	| Yellow | Very low (pLDDT < 50) |

3. A predicted aligned error plot (pae.png).  The confidence values for each residue are coloured using the same colour scheme as the PyMol session. 

## Feedback

Any and all feedback is welcome, just raise an issue and I'll get back to you!





