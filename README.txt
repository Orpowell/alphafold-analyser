# AlphaFold Analyser
This program produces high quality visualisations of predicted structures produced by 
AlphaFold. These visualisations allow the user to view the pLDDT of each residue of a protein
structure and the predicted alignment error for the entire protein to rapidly infer the 
quality of a predicted structure.

## Dependencies
- Python 3.7
- AlphaFold 2.0.0
- PyMol 2.5.2
- Matplotlib 3.4.2

## Installing AlphaFold Analyser on Linux & MacOSX
At the command line, change directory to the directory where alphafold-analyser.py was downloaded,
<download-directory>, using the full path name.

	cd <download-directory>

Now move the file to where you normally keep your binaries. This directory should be in
your path. Note: you may require administrative privileges to do this
(either switching user to root or by using sudo).

As root:

	mv alphafold-analyser.py /usr/local/bin/
	
As regular user:

	sudo mv alphafold-analyser.py /usr/local/bin/
	
A.V.A should now run from the shell or Terminal using the command ava.py

Alternatively, alphafold-analyser.py can be run directly from an IDE. 

## AlphaFold Settings for the Analyser
For the programme to function correctly, the model names parameter should label the first 
two models in alphafold as model_1 and model_2_ptm. An example of how this parameter should 
be written when running AlphaFold is shown below.

	--model_names=model_1,model_2_ptm,model_3,model_4,model_5 \
	
model_2_ptm is used to collect the data required to plot the Predicted Alignment Error.

All files output by alphafold are stored in a single directory. However, only
the ranked_0.pdb and results_model_2_ptm.pkl file are needed for analysis.

## Running AlphaFold Analyser
A directory should be created containing all necessary files (see above). AlphaFold Analyser
will then ask for the following inputs:

	- Input Directory: The file path for the directory containing the alphafold results files
	
	- Output Directory: The file path for the directory where the Analyser results will be
						stored.
						
	- Protein: The name of protein being analysed. This will be used to label all files
			   and the directory created during the analysis.

## Outputs
AlphaFold Analyser has produces two outputs:

A PyMol session, {Protein}.pse, containing the highest confidence predicted structure. The 
individual residues of the structure are coloured according to their pLDDT with the following
colour spectrum from low to high: 

							(Low Confidence) Yellow -> Green -> Blue (High Confidence)
							
A predicted alignment error plot, {protein}-pae.png, that colours the confidence values for
each residue using the same colour scheme shown above. 

## Comments
Future work may involve allowing for multiple inputs at once. 
