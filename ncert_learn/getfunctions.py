import ast
import os

def get_function_names_from_python_file(file_path):
    """Extract function names from a given Python file."""
    if not os.path.isfile(file_path):
        return False

    if not file_path.endswith(".py"):
        return False

    try:
        with open(file_path, "r") as file:
            file_content = file.read()
        
        # Parse the file content
        tree = ast.parse(file_content)
        
        # Extract function names
        function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        
        return ', '.join(function_names)  # Return function names as a comma-separated string
    except Exception as e:
        return False
