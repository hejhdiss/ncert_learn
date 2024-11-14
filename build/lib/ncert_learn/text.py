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
def addlinetofile(a):

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


def readspecificline( line_number):

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

    