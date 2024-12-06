import os
def istextfile(file_path):
    """
    Check if a file is a text file.
    
    Parameters:
    file_path (str): Path to the file.

    Returns:
    bool: True if the file is a text file, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read(1024)  # Read the first 1024 bytes as a test
        return True
    except (UnicodeDecodeError, IOError,EOFError):
        return False


def copytextfromonetoanother(a,b):

    """
    Copies the text from the file given by path a to the file given by path b.

    Parameters
    ----------
    a : str
        The path of the file to copy from.
    b : str
        The path of the file to copy to.

    Returns
    -------
    bool
        True if the copy operation is successful, False otherwise.
    """
    

    if not('str' in type(a)):
        return False
    if not('str' in type(b)):
        return False
    elif a=='':
        return False
    elif b=='':
        return False
    elif not(istextfile(a)):
        return False
    elif not(istextfile(b)):
        return False
    else:
        try:
            f1=open(a,'r')
            f2=open(b,'w')
            line=f1.readline()
            while line!='':
                f2.write(line)
                line=f1.readline()
            f1.close()
            f2.close()
        except FileNotFoundError:
            return False
        except FileExistsError:
            return False
        except Exception:
            return False
        else:
            return True
path=''
def opentextfile(a):

    """
    Opens the text file given by path a in the default text editor.

    Parameters
    ----------
    a : str
        The path of the file to open.

    Returns
    -------
    bool
        True if the file is opened successfully, False otherwise.
    """
    global path

    if not('str' in type(a)):
        return False    
    elif a=='':
        return False
    elif not(istextfile(a)):
        return False
    else:
        try:
            s=open(a,'r')
            path=a
            s.close()
        except FileNotFoundError:
            return False
        except Exception:
            return False
        else:
            return True
def addlinetotextfile(a):

    """
    Appends a line of text to the file opened by opentextfile() function.

    Parameters
    ----------
    a : str
        The line of text to append.

    Returns
    -------
    bool
        True if the line is appended successfully, False otherwise.
    """
    global path
    if path=='':
        return False
    elif not('str' in type(a)):    
        return False
    elif a=='':
        return False
    else:
        try:
            s=open(path,'a')
            s.write(f'{a}\n')
            s.close()
        except FileNotFoundError:
            return False
        except Exception:
            return False
        else:
            return True

def readtextfile(a):

    """
    Reads the contents of the file opened by opentextfile() function.

    Parameters
    ----------
    a : str
        Ignored.

    Returns
    -------
    str
        The contents of the file as a string.
    """
    global path
    

    s=open(path,'r')
    return s.read()
def cleartextfile():

    """
    Clears the contents of the file opened by opentextfile() function.

    """
    global path
    

    with open(path, "w") as file:
        pass


def readspecificlinetextfile( line_number):

    """
    Reads a specific line from the file opened by opentextfile() function.

    Parameters
    ----------
    line_number : int
        The line number to read from the file (1-based index).

    Returns
    -------
    str
        The content of the specified line as a string if successful.
    bool
        False if the file is not found, line number is out of range, or any other exception occurs.
    """
    global path

    try:
        # Open the file in read mode
        with open(path, "r") as file:
            # Read all lines into a list
            lines = file.readlines()
            
            # Check if the line number is within the valid range
            if line_number <= 0 or line_number > len(lines):
                raise False
            
            # Print the specific line
            return lines[line_number - 1].strip()  # Using line_number - 1 for 0-based indexing
    except FileNotFoundError:       
        return False
    except EOFError:
        return False
    except IndexError as e:
        return False
    except Exception as e:
        return False
def modifyspecificlinetextfile(line_number, new_content):
    """
    Modifies a specific line in the file opened by opentextfile() function.

    Parameters
    ----------
    line_number : int
        The line number to modify (1-based index).
    new_content : str
        The new content to replace the specified line with.

    Returns
    -------
    bool
        True if the line was successfully modified, False if the file is not found, line number is out of range, or any other exception occurs.
    """
    global path

    try:
        # Open the file in read mode
        with open(path, "r") as file:
            lines = file.readlines()

        # Check if the line number is within the valid range
        if line_number <= 0 or line_number > len(lines):
            return False

        # Modify the specified line
        lines[line_number - 1] = new_content + '\n'  # Ensure the line ends with a newline character

        # Write the modified lines back to the file
        with open(path, "w") as file:
            file.writelines(lines)

        return True
    except (FileNotFoundError, IOError,EOFError):
        return False
    except Exception as e:
        return False

def overwritetextfile(new_content):
    """
    Overwrites the contents of the currently opened text file with new content.

    Parameters
    ----------
    new_content : str
        The new content to write to the file.

    Returns
    -------
    bool
        True if the operation is successful, False otherwise.
    """
    global path

    if not path or not isinstance(new_content, str):
        return False

    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        return True
    except (FileNotFoundError, IOError, Exception):
        return False
import os

def text_file_operations_advanced_mode(folder_path, operation, file_name=None, new_name=None, data=None):
    """
    Perform various text file operations in a specified folder.

    Parameters
    ----------
    folder_path : str
        Path to the folder where the operations will be performed.
    operation : str
        The operation to perform. Supported operations:
        'create', 'write', 'append', 'read', 'clear', 'delete', 'rename', 'list_files', 'overwrite'.
    file_name : str, optional
        The file name for the operation.
    new_name : str, optional
        New name for the file (used in 'rename').
    data : str, optional
        Text data for 'write', 'append', or 'overwrite' operations.

    Returns
    -------
    bool or str or list
        - For 'read': Returns file content (str) or False on error.
        - For 'list_files': Returns a list of files in the folder or False on error.
        - For other operations: Returns True on success, False on failure.
    """
    # Validate folder path
    if not folder_path or not os.path.isdir(folder_path):
        return False

    try:
        file_path = os.path.join(folder_path, file_name) if file_name else None

        # Create a new text file
        if operation == 'create':
            if not file_name:
                return False
            with open(file_path, 'w', encoding='utf-8') as file:
                pass  # Create an empty text file
            return True

        # Write text data to a file
        elif operation == 'write':
            if not file_name or data is None or not isinstance(data, str):
                return False
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)
            return True

        # Append text data to a file
        elif operation == 'append':
            if not file_name or data is None or not isinstance(data, str):
                return False
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(data)
            return True

        # Overwrite the file with new content
        elif operation == 'overwrite':
            if not file_name or data is None or not isinstance(data, str):
                return False
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)
            return True

        # Read text file content
        elif operation == 'read':
            if not file_name:
                return False
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()

        # Clear text file content
        elif operation == 'clear':
            if not file_name:
                return False
            with open(file_path, 'w', encoding='utf-8') as file:
                pass  # Overwrite with an empty file
            return True

        # Delete a text file
        elif operation == 'delete':
            if not file_name:
                return False
            os.remove(file_path)
            return True

        # Rename a text file
        elif operation == 'rename':
            if not file_name or not new_name:
                return False
            new_file_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_file_path)
            return True

        # List all files in the folder
        elif operation == 'list_files':
            return [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        else:
            return False  # Unsupported operation

    except (FileNotFoundError, IOError, OSError):
        return False

    