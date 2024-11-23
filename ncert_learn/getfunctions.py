import ast
import os

def get_function_names_from_python_file_str(file_path):


    """
    Extract function names from a given Python file.

    Args:
        file_path (str): Path to the Python file.

    Returns:
        str: Function names as a comma-separated string, or False on error.
    """


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

def get_function_names_from_python_file_list(file_path):
    """
    Extract function names from a given Python file.

    Args:
        file_path (str): Path to the Python file.

    Returns:
        list: List of function names, or False on error.
    """
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
        
        return function_names
    except Exception as e:
        return False


