import networkx as nx


def build_zoo(max_n=10):
    """
    Construit un zoo diversifié de graphes connexes.
    Compatible NetworkX >= 3.4
    """
    zoo = []

    for n in range(2, max_n + 1):

        # 1️⃣ Chemin
        zoo.append(nx.path_graph(n))

        # 2️⃣ Cycle
        if n >= 3:
            zoo.append(nx.cycle_graph(n))

        # 3️⃣ Complet
        zoo.append(nx.complete_graph(n))

        # 4️⃣ Arbre aléatoire (CORRIGÉ)
        zoo.append(nx.random_labeled_tree(n))

        # 5️⃣ Biparti complet
        if n >= 4:
            k = n // 2
            zoo.append(nx.complete_bipartite_graph(k, n - k))

        # 6️⃣ Graphe aléatoire connexe
        G = nx.gnp_random_graph(n, 0.4, seed=42)
        if nx.is_connected(G):
            zoo.append(G)

    return zoo
