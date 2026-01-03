import matplotlib.pyplot as plt
import networkx as nx
import os


def show_graph(G, title="", save_path=None, show=True):
    """
    Dessine un graphe. Sauvegarde si save_path est donné.
    Affiche seulement si show=True (important pour multi-essais).
    """
    fig = plt.figure(figsize=(5, 5))

    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=500,
        font_size=8
    )

    if title:
        plt.title(title)

    if save_path:
        folder = os.path.dirname(save_path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        plt.savefig(save_path)
        print(f"📸 Image sauvegardée : {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)
