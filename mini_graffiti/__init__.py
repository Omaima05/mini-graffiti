from zoo import build_zoo
from tester import test_conjecture
from llm import generate_formula
from visualizer import show_graph
from database import (
    save_conjecture,
    get_valid_conjectures,
    get_invalid_conjectures
)


def ask_ai_for_formula():
    """
    Demande une nouvelle conjecture au modèle LLM (Gemini).
    """
    print("\n🤖 Génération d'une nouvelle conjecture…")
    formula = generate_formula()
    print(f"💡 Conjecture proposée : {formula}")
    return formula


def test_formula_on_zoo(formula, zoo):
    """
    Teste une conjecture sur le Zoo.
    Enregistre le résultat dans la base SQLite.
    """
    print("\n🧪 Test de la conjecture sur le Zoo…")

    ok, counterexample_index = test_conjecture(formula, zoo)

    if ok:
        print("✅ Conjecture validée sur tout le Zoo !")
        save_conjecture(formula, True)
    else:
        print("❌ Conjecture réfutée !")
        print(f"   ➤ Contre-exemple : Graphe #{counterexample_index}")

        save_conjecture(
            formula,
            False,
            notes=f"Graphe #{counterexample_index}"
        )

    return ok, counterexample_index


def show_report(zoo):
    """
    Affiche un rapport clair :
    - Conjectures validées
    - Conjectures invalides avec visualisation des contre-exemples
    """
    print("\n📚 ===== RAPPORT COMPLET =====\n")

    # 🔵 VALIDÉES
    valides = get_valid_conjectures()
    print("🟢 Conjectures validées :")
    if not valides:
        print("   ➤ Aucune pour l'instant.")
    else:
        for formula, tested_on in valides:
            print(f"   ✓ {formula}   (testée le {tested_on})")

    # 🔴 INVALIDES
    print("\n🔴 Conjectures invalides :")
    invalides = get_invalid_conjectures()

    if not invalides:
        print("   ➤ Aucune pour l'instant.")
    else:
        for formula, notes, tested_on in invalides:
            print(f"   ✗ {formula}   (testée le {tested_on})")
            print(f"     ➤ Contre-exemple : {notes}")

            # Visualisation automatique
            if notes.startswith("Graphe #"):
                try:
                    idx = int(notes.split("#")[1])
                    show_graph(
                        zoo[idx],
                        title=f"Contre-exemple pour : {formula}"
                    )
                except Exception as e:
                    print("⚠ Erreur de visualisation :", e)


def main():
    print("🚀 MINI-GRAFFITI — SYSTÈME DE CONJECTURES AUTOMATISÉ")
    print("====================================================")

    # 1️⃣ Charger le Zoo de graphes
    print("\n📦 Construction du Zoo…")
    zoo = build_zoo()
    print(f"   ➤ {len(zoo)} graphes chargés !")

    # 2️⃣ Générer une conjecture via Gemini
    formula = ask_ai_for_formula()

    # 3️⃣ Tester la conjecture
    ok, _ = test_formula_on_zoo(formula, zoo)

    # 4️⃣ Afficher le rapport complet
    show_report(zoo)


if __name__ == "__main__":
    main()
