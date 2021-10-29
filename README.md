<h1 id="alphafold-analyser">AlphaFold Analyser</h1>
<p>This program produces high quality visualisations of predicted structures produced by AlphaFold. These visualisations allow the user to view the pLDDT of each residue of a protein structure and the predicted alignment error for the entire protein to rapidly infer the quality of a predicted structure.</p>
<h2 id="dependencies">Dependencies</h2>
<ul>
<li>Python 3.7</li>
<li>AlphaFold 2.0.0</li>
<li>PyMol 2.5.2</li>
<li>Matplotlib 3.4.2</li>
</ul>
<h2 id="installing-alphafold-analyser-on-linux-macosx">Installing AlphaFold Analyser on Linux &amp; MacOSX</h2>
<p>At the command line, change directory to the directory where alphafold-analyser.py was downloaded, <download-directory>, using the full path name.</p>
<pre><code>cd &lt;download-directory&gt;</code></pre>
<p>Now move the file to where you normally keep your binaries. This directory should be in your path. Note: you may require administrative privileges to do this (either switching user to root or by using sudo).</p>
<p>As root:</p>
<pre><code>mv alphafold-analyser.py /usr/local/bin/</code></pre>
<p>As regular user:</p>
<pre><code>sudo mv alphafold-analyser.py /usr/local/bin/</code></pre>
<p>A.V.A should now run from the shell or Terminal using the command ava.py</p>
<p>Alternatively, alphafold-analyser.py can be run directly from an IDE.</p>
<h2 id="alphafold-settings-for-the-analyser">AlphaFold Settings for the Analyser</h2>
<p>For the programme to function correctly, the model names parameter should label the first two models in alphafold as model_1 and model_2_ptm. An example of how this parameter should be written when running AlphaFold is shown below.</p>
<pre><code>--model_names=model_1,model_2_ptm,model_3,model_4,model_5 \</code></pre>
<p>model_2_ptm is used to collect the data required to plot the Predicted Alignment Error.</p>
<p>All files output by alphafold are stored in a single directory. However, only the ranked_0.pdb and results_model_2_ptm.pkl file are needed for analysis.</p>
<h2 id="running-alphafold-analyser">Running AlphaFold Analyser</h2>
<p>A directory should be created containing all necessary files (see above). AlphaFold Analyser will then ask for the following inputs:</p>

Input Directory: The file path for the directory containing the alphafold results files

Output Directory: The file path for the directory where the Analyser results will be
                    stored.
                    
Protein: The name of protein being analysed. This will be used to label all files
           and the directory created during the analysis


<h2 id="outputs">Outputs</h2>
<p>AlphaFold Analyser has produces two outputs:</p>

<p> - A PyMol session labelled with the protein input (e.g protein.pse). This will  contain the highest confidence structure predicted by AlphaFold. The individual residues of the structure are coloured according to their pLDDT on colour spectrum from yellow to green to blue (low to high confidence).<p>

<p> - A predicted alignment error plot again labelled with the protein input (e.g protein-pae.png). The plot is colored by the confidence values for each residue using the same colour scheme as the PyMol session.</p>
<h2 id="comments">Comments</h2>
<p>Future work may involve allowing for multiple inputs at once.</p>
