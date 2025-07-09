# AlphaFold Analyser

AlphaFold Analyser is a command line tool that produces publication quality visualisations of AlphaFold2 and AlphaFold3 predictions. These visualisations allow the user to view the pLDDT and predicted alignment error (PAE) of predictions and rapidly infer their quality. Alphafold analyser can process the results of monomer and multimeric predictions.

## Installing AlphaFold Analyser

AlphaFold Analyser can be easily installed using conda and the following commands:

	conda create -n alphafold-analyser python=3.10.16
	conda install conda-forge::pymol-open-source

	conda activate alphafold-analyser
	git clone https://github.com/Orpowell/alphafold-analyser.git
	cd alphafold-analyser
	pip install .

## Running AlphaFold Analyser

Three commands are available using alphafold-analyser [pae, plddt, structure]. All commands can be run in a conda environment (see above) as follows:

	conda activate alphafold-analyser
	alphafold-analyser <command>

## PAE

The pae command generates a predicted aligned error (PAE) plot of a prediction. In AlphaFold2, PAE data is stored in a predictions PKL file. In AlphaFold3, PAE data is stored in a predictions "full_data" Json file. To analyse AlphaFold3 predictions specify the "--alphafold3" flag. AlphaFold3 predictions also contain a contact probability map that can be visualised using the "--plot_contacts" flag.

AlphaFold2:

	alphafold-analyser pae \
		--data prediction.pkl \
		--output pae.png

AlphaFold3:

	alphafold-analyser pae \
		--data prediction_full_data_x.json \
		--output pae.png \
		--alphafold3

AlphaFold3 contact map:

	alphafold-analyser pae \
		--data prediction_full_data_x.json \
		--output pae.png \
		--alphafold3 \
		--plot_contacts

### Parameters

The pae command accepts the following arguments:

| Argument | Short | Description |
|----------|-------|-------------|
| `--data` | `-d` | Path to prediciton data: *.pkl (AF2) or *.json (AF3). |
| `--output` | `-o` | Path for output PAE plot (default: "pae.png"). |
| `--alphafold3` | `-af3` | Specify for AlphaFold3 prediction analysis. |
| `--plot_contacts` | `-pc` | AlphaFold3 only: Plot contact map instead of PAE plot. |
| `--help` | `-h` | Show help message and exit. |

## PLDDT

The plddt command generates a plddt plot of a prediction. In AlphaFold2, plddt data is stored in a predictions PKL file. In AlphaFold3, plddt data is stored in a predictions "full_data" Json file. To analyse AlphaFold3 predictions specify the "--alphafold3" flag. AlphaFold3 stores plddt per atom instead of plddt per residue. This can make AlphaFold3 plddt plots harder to interpret without a corresponding structure (see: Structure). For AlphaFold2-Multimer predictions predicted TM-score (pTM) and Interface predicted TM-score (ipTM) scores are also reported. These scores are not reported in AlphaFold3 predictions but can be found in the "summary confidences" Json file for each prediction. 

AlphaFold2:

	alphafold-analyser pae \
		--data prediction.pkl \
		--output pae.png

AlphaFold3:

	alphafold-analyser pae \
		--data prediction_full_data_x.json \
		--output pae.png \
		--alphafold3

### Parameters

The plddt command accepts the following arguments:

| Argument | Short | Description |
|----------|-------|-------------|
| `--data` | `-d` | Path to prediciton data: *.pkl (AF2) or *.json (AF3). |
| `--output` | `-o` | Path for output PLDDT plot (default: "plddt.png"). |
| `--alphafold3` | `-af3` | Specify for AlphaFold3 prediction analysis. |
| `--help` | `-h` | Show help message and exit. |

## Structure

The structure command creates a PyMol session of a prediction and colours the prediction using plddt values. The command works with both \*.cif and \*.pdb files. Unlike, the pae and plddt commands, the version of AlphaFold used does not need to be specified. On linux systems, the location of your PyMol binary can be found using the command *where pymol*. We recommend using the open-source binary installed in the conda environment (See: Installing AlphaFold Analyser).

	alphafold-analyser pae \
		--structure prediction.pdb \
		--binary /path/to/pymol/binary \
		--output plddt.pse \

### Parameters

The structure command accepts the following arguments:

| Argument | Short | Description |
|----------|-------|-------------|
| `--structure` | `-s` | Path to prediciton structure [*.pdb *.cif]. |
| `--output` | `-o` | Path for output pymol session (default: "plddt.pse"). |
| `--binary` | `-b` | Path to PyMol binary. |
| `--help` | `-h` | Show help message and exit. |

### Plddt Colour Scheme

| Colour | pLDDT confidence |
|---|---|
| Blue  | Very high (pLDDT > 90) |
| Cyan 	| High (90 > pLDDT > 70) |
| Orange | Low (70 > pLDDT > 50) |
| Yellow | Very low (pLDDT < 50) |

## Command Outputs

![outputs](https://github.com/orpowell/alphafold-analyser/blob/main/img/outputs.png)

AlphaFold Analyser can create the following outputs:

A) A plot of pLDDT across the structure generated using the plddt command. This shows the plddt confidence score across the sequence with color coding. 

B) A PyMol session generated using the structure command. This contains the predicted structure coloured according to pLDDT.

C) A predicted aligned error plot generated using the pae command. The confidence values for each residue are colored using a green color gradient. Lower values (darker green) indicate higher confidence in the predicted alignment. For AlphaFold3 predictions, a contact map (not shown) can also be created with an inverted colour scheme in which higher probability contacts are coloured darker green.


## Citing AlphaFold Analyser

If you use this tool or the associated source code please cite:

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

Please also cite the relevant AlphaFold papers as necessary.
