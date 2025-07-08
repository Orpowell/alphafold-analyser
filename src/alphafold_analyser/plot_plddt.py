from .utils import depickler
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from .utils import multimer_stats

# Plot plDDT
def plot_pLDDT(pickle, output):
    
    data = depickler(pickle_input=pickle)
    
    fig, ax = plt.subplots(figsize=(20, 5))

    plddt = data["plddt"]
    max_length = len(plddt) + (len(plddt) * 0.1)
    position = [n + 1 for n, ele in enumerate(data["plddt"])]

    # Confidence boundaries
    ax.add_patch(Rectangle((0, 90), max_length, 10, color="#024fcc"))
    ax.add_patch(Rectangle((0, 70), max_length, 20, color="#60c2e8"))
    ax.add_patch(Rectangle((0, 50), max_length, 20, color="#f37842"))
    ax.add_patch(Rectangle((0, 0), max_length, 50, color="#f9d613"))

    ax.plot(
        position,
        plddt,
        color="black",
        linewidth=2,
        linestyle="-"
    )

    ax.set_ylim(0, 100)
    ax.set_xlim(1, max(position) + 10)
    ax.spines[["right", "top"]].set_visible(False)
    ax.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    plddt_legend = {
        "Very high (pLDDT > 90)": "#024fcc",
        "High (90 > pLDDT > 70)": "#60c2e8",
        "Low (70 > pLDDT > 50)": "#f37842",
        "Very low (pLDDT < 50)": "#f9d613",
    }

    ax.legend(plddt_legend, title="pLDDT Confidence", prop={'size': 16}, bbox_to_anchor=(-0.05, 1))

    ax.set_xlabel("Amino Acid Position")
    ax.set_ylabel("pLDDT")
    
    if 'iptm' in data.keys():
        multimer_stats(data)

    plt.savefig(f"{output}", dpi=300, bbox_inches="tight")

