import ast

ALLOWED_NODES = (
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.Compare,
    ast.Name, ast.Load, ast.Constant,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod,
    ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.Eq, ast.NotEq,
)

def safe_eval(expr: str, variables: dict) -> bool:
    try:
        tree = ast.parse(expr, mode="eval")
        for node in ast.walk(tree):
            if not isinstance(node, ALLOWED_NODES):
                return False
            if isinstance(node, ast.Name) and node.id not in variables:
                return False
        code = compile(tree, "<expr>", "eval")
        return bool(eval(code, {"__builtins__": {}}, variables))
    except Exception:
        return False