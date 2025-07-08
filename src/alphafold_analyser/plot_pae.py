from .utils import depickler, load_json

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Plot Predicted Aligned Error
def plot_PAE(pickle:str, output:str, alphafold3:bool, plot_contacts:bool):
    
    if not alphafold3:
        data = depickler(pickle_input=pickle)
    
    if alphafold3:
        data = load_json(input=pickle)
        data["predicted_aligned_error"] = data['pae']
        
        if plot_contacts:
            data["predicted_aligned_error"] = data['contact_probs']
            
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_facecolor("white")  
    cmap = ax.imshow(
        data["predicted_aligned_error"],
        vmin=0,
        vmax=max(max(v) for v in data["predicted_aligned_error"]),
        cmap="Greens_r",
    )  
    ax.set_xlabel("Scored residue")  
    ax.set_ylabel("Aligned residue")  

    axins = inset_axes(ax, width="100%", height="5%", loc="lower center", borderpad=-7)

    cbar = fig.colorbar(cmap, cax=axins, orientation="horizontal")  
    cbar.set_label("Expected position error (Ångströms)")

    plt.savefig(f"{output}", dpi=300, bbox_inches="tight")