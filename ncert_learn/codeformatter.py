import autopep8
import pylint.lint
import io
import sys

# --------------------------- Code Formatter ---------------------------

def format_code(source_code):
    """Formats Python code according to PEP 8 style guide."""
    try:
        formatted_code = autopep8.fix_code(source_code)
        return formatted_code
    except:
        return False

# --------------------------- Code Linter ---------------------------

def lint_code(source_code):
    """Lints Python code to check for potential issues and follows PEP 8."""
    try:
        # Redirect stdout to capture pylint output
        output = io.StringIO()
        sys.stdout = output

        # Create a dummy file to pass to pylint
        with open('temp_code.py', 'w') as f:
            f.write(source_code)

        # Run pylint on the code
        pylint_opts = ['temp_code.py']
        pylint.lint.Run(pylint_opts)

        lint_output = output.getvalue()
        sys.stdout = sys.__stdout__  # Reset stdout

        # Clean up the temporary file
        try:
            import os
            os.remove('temp_code.py')
        except:
            pass

        return lint_output
    except:
        return False

# --------------------------- Utility Functions ---------------------------

def check_code_quality(source_code):
    """Checks the overall quality of the Python code."""
    try:
        lint_output = lint_code(source_code)
        if lint_output:
            issues = lint_output.split('\n')
            if len(issues) > 0:
                return "Code has issues:\n" + '\n'.join(issues)
            else:
                return "Code is clean according to PEP 8 standards."
        else:
            return "Linting failed. Please check the code."
    except:
        return False

def fix_and_lint_code(source_code):
    """Formats and lints the Python code."""
    try:
        formatted_code = format_code(source_code)
        lint_output = lint_code(formatted_code)
        if formatted_code and lint_output:
            return formatted_code, lint_output
        else:
            return False
    except:
        return False
