# AlphaFold Analyser

AlphaFold Analyser is a command line tool to produce high quality visualisations of protein structures predicted by AlphaFold2. These visualisations allow the user to view the pLDDT of each residue of a protein structure and the predicted alignment error for the entire protein to rapidly infer the quality of a predicted structure. Alphafold analyser can process the results of both multimer and monomer predictions.

The following software is required:
- Python >= 3.7
- PyMol == 2.5.2
- Matplotlib==3.5.1

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

## Usage

**NOTE**: to plot the predicted aligned error of a monomer; AlphaFold must be run using the setting —model_preset=monomer_ptm (ptm models are automatically generated for multimer predictions).

When running alphafold analyser, please ensure the structure and pickle file used are for the same prediction. All commands require an output directory to be specified (-o or —output_directory) and can be run simultaneously.  

```
alphafold-analyser.py \
	--pkl protein.pkl \
	--pdb protein.pdb \
	--binary path/to/pymol/binary \
	--output output_directory
```

### Command Line Arguments

The script accepts the following command line arguments:

| Argument | Short | Description |
|----------|-------|-------------|
| `--pdb` | `-p` | Path to PDB file - generates pLDDT colored structure visualization |
| `--pkl` | `-l` | Path to pickle file - generates predicted aligned error plot |
| `--binary` | `-b` | Path to PyMOL binary - required when analyzing PDB files |
| `--output` | `-o` | Directory to store all generated outputs (default: "analyser_output") |
| `--version` | `-v` | Show program version and exit |
| `--help` | `-h` | Show help message and exit |

### Creating a pLDDT annotated structure
A pLDDT annotated structure can be generated using the following command:

```
alphafold-analyser.py \
	--pdb protein.pdb \
	--binary path/to/pymol/binary \
	--output my_directory
```

### Generating a predicted alignment error and pLDDT plot
A PAE plot can be generated using the following command:


	alphafold-analyser.py \
		--pkl protein.pkl \
		--output my_directory


### Running both analyses simultaneously
You can run both analyses in a single command:


	alphafold-analyser.py \
		--pkl protein.pkl \
		--pdb protein.pdb \
		--binary path/to/pymol/binary \
		--output my_directory


## Outputs

![outputs](https://github.com/orpowell/alphafold-analyser/blob/main/img/outputs.png)

AlphaFold Analyser creates the following outputs:

1. A plot of pLDDT across the structure (`plddt.png`): Shows the per-residue confidence scores across the sequence with color coding.

2. A PyMol session (`pLDDT.pse`): This will contain the structure predicted by AlphaFold with each individual residues coloured according to their pLDDT as follows:

	| Colour | pLDDT confidence |	
	|---|---|
	| Blue  | Very high (pLDDT > 90) |
	| Cyan 	| High (90 > pLDDT > 70) |
	| Orange | Low (70 > pLDDT > 50) |
	| Yellow | Very low (pLDDT < 50) |

3. A predicted aligned error plot (`PAE.png`): The confidence values for each residue are colored using a green color gradient. Lower values (darker green) indicate higher confidence in the predicted alignment.

### Multimer Statistics

When analyzing multimer predictions, the tool also outputs the following statistics:

- **pTM**: A confidence metric for the predicted TM-score of the model
- **ipTM**: Interface predicted TM-score, measures the confidence of the interface between chains

<br>

## Citing AlphaFold Analyser

If you use this code or tool please cite:

	@article {Hafeez2023,
		author = {Hafeez, Amber N. and Chartrain, Laetitia and Feng, Cong and Cambon, Florence and Clarke, Martha and Griffiths, Simon and Hayta, Sadiye and Jiang, Mei and Keller, Beat and Kirby, Rachel and Kolodziej, Markus C. and Powell, Oliver R. and Smedley, Mark and Steuernagel, Burkhard and Xian, Wenfei and Wingen, Luzie U. and Cheng, Shifeng and Saintenac, Cyrille and Wulff, Brande B. H. and Brown, James K. M.},
		title = {Septoria tritici blotch resistance gene Stb15 encodes a lectin receptor-like kinase},
		elocation-id = {2023.09.11.557217},
		year = {2023},
		doi = {10.1101/2023.09.11.557217},
		publisher = {Cold Spring Harbor Laboratory},
		URL = {https://www.biorxiv.org/content/early/2023/09/12/2023.09.11.557217},
		eprint = {https://www.biorxiv.org/content/early/2023/09/12/2023.09.11.557217.full.pdf},
		journal = {bioRxiv}
	}

In addition please also cite the AlphaFold papers as necessary.

