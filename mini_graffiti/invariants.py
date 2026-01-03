import networkx as nx

def compute_invariants(G):
    inv = {}
    n = G.number_of_nodes()
    m = G.number_of_edges()
    inv["nb_noeuds"] = n
    inv["nb_aretes"] = m

    # composantes connexes
    if n == 0:
        inv["nb_composantes"] = 0
    else:
        inv["nb_composantes"] = nx.number_connected_components(G) if not G.is_directed() else 1

    # degrés
    if n > 0:
        degres = [d for _, d in G.degree()]
        inv["degre_min"] = min(degres)
        inv["degre_max"] = max(degres)
        inv["degre_moyen"] = sum(degres) / n
    else:
        inv["degre_min"] = 0
        inv["degre_max"] = 0
        inv["degre_moyen"] = 0

    # densité
    inv["densite"] = nx.density(G) if n > 1 else 0

    # diamètre / rayon
    if n > 0 and nx.is_connected(G):
        inv["diametre"] = nx.diameter(G)
        inv["rayon"] = nx.radius(G)
    else:
        inv["diametre"] = float("inf")
        inv["rayon"] = float("inf")

    # complexité cyclomatique (m - n + c)
    c = inv["nb_composantes"]
    inv["cyclomatic"] = m - n + c

    return inv

