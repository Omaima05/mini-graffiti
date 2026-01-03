from invariants import compute_invariants
from parser import safe_eval

def find_best_counterexample(formula, zoo):
    failures = []
    for i, G in enumerate(zoo):
        inv = compute_invariants(G)
        if not safe_eval(formula, inv):
            failures.append((i, inv["nb_noeuds"], inv["nb_aretes"]))
    if not failures:
        return None
    failures.sort(key=lambda x: (x[1], x[2]))  # n puis m
    return failures[0][0]  # index du meilleur contre-exemple

def test_conjecture(formula, zoo):
    idx = find_best_counterexample(formula, zoo)
    if idx is None:
        return True, None
    return False, idx
