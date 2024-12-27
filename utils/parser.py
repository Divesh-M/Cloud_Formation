import ast

def parse_code(code):
    """
    Parses Python code to extract functions, arguments, and docstrings.

    Args:
        code (str): The Python code as a string.

    Returns:
        list: A list of dictionaries containing function details.
    """
    try:
        tree = ast.parse(code)
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_details = {
                    "name": node.name,
                    "args": [arg.arg for arg in node.args.args],
                    "docstring": ast.get_docstring(node) or "No docstring provided.",
                }
                functions.append(func_details)
        return functions
    except Exception as e:
        print(f"Error parsing code: {e}")
        return []
