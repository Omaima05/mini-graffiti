import networkx as nx

from datetime import datetime
from zoo import build_zoo
from llm import generate_formula
from tester import test_conjecture
from invariants import compute_invariants
from visualizer import show_graph
from database import save_conjecture, get_all_conjectures
import random
random.seed(42)

def get_solid_zoo(max_n=10):
    """
    Construit un zoo de graphes connexes (solides).
    """
    zoo = build_zoo(max_n=max_n)
    zoo_solide = [G for G in zoo if nx.is_connected(G) and G.number_of_nodes() > 1]
    return zoo_solide


def run_conjecture_session(nb_tentatives=20):
    print("\n🚀 MINI-GRAFFITI — SESSION MULTI-CONJECTURES")
    print("=" * 55)

    zoo_solide = get_solid_zoo(max_n=10)
    print(f"📦 Zoo construit : {len(zoo_solide)} graphes connexes")

    if not zoo_solide:
        print("❌ Aucun graphe valide dans le zoo.")
        return

    historique = []

    nb_valides = 0
    nb_refutees = 0

    for t in range(1, nb_tentatives + 1):
        print(f"\n--- Tentative {t}/{nb_tentatives} ---")

        # Générer une conjecture (en évitant les répétitions)
        formula = generate_formula(", ".join(historique))
        historique.append(formula)

        print(f"💡 Conjecture : {formula}")

        # Tester
        is_true, counterexample_index = test_conjecture(formula, zoo_solide)

        if is_true:
            nb_valides += 1
            print("✅ VALIDÉE sur tout le zoo.")

            note_text = (
                f"TYPE=VALIDEE | Zoo_size={len(zoo_solide)} | "
                f"Aucun contre-exemple trouvé"
            )
            save_conjecture(formula, True, notes=note_text)

            # Affiche 1 fois sur 5 pour pas spam
            if t % 5 == 0:
                G = random.choice(zoo_solide)
                show_graph(G, title=f"EXEMPLE VALIDE : {formula}")

        else:
            nb_refutees += 1
            G_ce = zoo_solide[counterexample_index]
            inv = compute_invariants(G_ce)

            stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_path = f"rapport/images/ce_{counterexample_index}_{stamp}.png"

            note_text = (
                f"TYPE=REFUTEE | Zoo_size={len(zoo_solide)} | "
                f"Contre-exemple=Graphe #{counterexample_index} | "
                f"n={inv['nb_noeuds']}, m={inv['nb_aretes']}, "
                f"d={inv['diametre']}, r={inv['rayon']}, "
                f"dmin={inv['degre_min']}, dmax={inv['degre_max']} | "
                f"image={image_path}"
            )

            save_conjecture(formula, False, notes=note_text)
            print(f"❌ RÉFUTÉE (contre-exemple #{counterexample_index})")

            # Afficher/sauver le contre-exemple
            show_graph(G_ce, title=f"CONTRE-EXEMPLE : {formula}", save_path=image_path, show=False)


    print("\n" + "=" * 55)
    print(f"✅ BILAN : {nb_valides} validées / {nb_refutees} réfutées")
    total = nb_valides + nb_refutees
    print("\n📊 SYNTHÈSE AUTOMATIQUE")
    print(f"Conjectures testées : {total}")
    print(f"Validées : {nb_valides}")
    print(f"Réfutées : {nb_refutees}")
    print("=" * 55)

def afficher_bilan_db():
    """
    Affiche toutes les conjectures enregistrées.
    """
    print("\n📊 BILAN DE LA BASE DE DONNÉES")
    print("=" * 40)

    rows = get_all_conjectures()
    if not rows:
        print("Aucune conjecture enregistrée.")
        return

    for formula, is_true, tested_on, notes in rows:
        statut = "✅ VALIDE" if is_true else "❌ RÉFUTÉE"
        print(f"{statut} : {formula}")
        print(f"  Date : {tested_on}")
        print(f"  Notes : {notes}")
        print("-" * 40)


historique = []
...
formula = generate_formula(", ".join(historique))
historique.append(formula)

if __name__ == "__main__":
    run_conjecture_session(nb_tentatives=20)
    afficher_bilan_db()
