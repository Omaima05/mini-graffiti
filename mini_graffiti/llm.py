import re
import time
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def clean_formula(text: str) -> str:
    # On prend la première ligne non vide
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
    if not lines:
        return ""
    line = lines[0]
    line = line.replace("`", "").replace("\\n", "").strip()
    return line

def looks_like_formula(s: str) -> bool:
    # Doit contenir un opérateur de comparaison
    if not any(op in s for op in ["<=", ">=", "<", ">", "==", "!="]):
        return False

    # Liste noire de mots-clés dangereux
    forbidden = ["import", "__", "os.", "sys.", "open(", "exec", "eval"]
    if any(x in s for x in forbidden):
        return False

    # Expression régulière pour n'autoriser que les calculs sûrs
    if not re.fullmatch(r"[A-Za-z0-9_+\-*/().<>=! \t]+", s):
        return False

    return True

def generate_formula(eviter_ceci=""):
    prompt = f"""
Tu es un assistant de recherche en théorie des graphes (Mini-Graffiti).
Propose UNE SEULE conjecture sous forme d'inégalité Python.

Variables autorisées :
nb_noeuds, nb_aretes, diametre, rayon,
degre_min, degre_max, degre_moyen, densite, cyclomatic.

Contraintes STRICTES :
- Une seule ligne
- Aucun texte explicatif
- Aucune ponctuation inutile
- Conjecture NON TRIVIALE
- Combine au moins deux variables différentes
- Évite les conjectures déjà testées : {eviter_ceci}

Format attendu (exemple) : diametre <= 2 * rayon
"""

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    last_error = None

    for _ in range(3):  # Tentatives en cas d'échec
        try:
            r = requests.post(OLLAMA_URL, json=payload, timeout=120)
            r.raise_for_status()

            raw = r.json().get("response", "")
            formula = clean_formula(raw)

            if looks_like_formula(formula):
                return formula

            # Si la réponse est mal formatée, on durcit la consigne
            payload["prompt"] += "\nRAPPEL : réponds uniquement par UNE inégalité Python."

        except Exception as e:
            last_error = e
            time.sleep(1.5)

    raise Exception(f"Erreur lors de la génération de la conjecture : {last_error}")