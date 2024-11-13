import os
import platform
import socket
import sys
def getexecutablepath():

    """
    Returns the list of directories that are used to search for executables.
    This is typically the system's PATH environment variable.
    """

    return os.get_exec_path()
def cpucount():

    """
    Returns the number of CPUs in the system.
    This function relies on the os module to determine
    the count of available CPUs.
    """

    return os.cpu_count()
def listdir():

    """
    Returns a list containing the names of the entries in the directory given by the path.
    The list is in arbitrary order. It does not include the special entries '.' and '..'
    even if they are present in the directory.

    This function relies on the os module to list the entries in the directory.
    """

    return os.listdir
def listdirfrompath(a):

    """
    Returns a list containing the names of the entries in the directory given by the path.
    The list is in arbitrary order. It does not include the special entries '.' and '..'
    even if they are present in the directory.

    This function relies on the os module to list the entries in the directory.

    Parameters
    ----------
    a : str
        The path of the directory to list.

    Returns
    -------
    list
        A list of the names of the entries in the directory.
    """

    if not('str' in str(type(a))):
        return False
    elif a=='':
        return False
    else:
        try:
            s=os.listdir(a)
        except FileNotFoundError:
            return False
        except Exception:
            return False
        else:
            return s
def osname():

    """
    Returns the name of the operating system.

    Returns
    -------
    str
        The name of the operating system.
    """

    return platform.system()
def processorname():

    """
    Returns the name of the processor.

    Returns
    -------
    str
        The name of the processor.
    """

    return platform.processor()
def isnetworkconnected():
    """
    Checks if the machine is connected to the internet.

    Returns
    -------
    bool
        True if the machine is connected to the internet, False otherwise.
    """

    try:
        # Try to connect to Google's DNS server
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False  
def getpythoninterpreter():

    """
    Returns the path to the Python interpreter executable.

    This function relies on the sys module to determine
    the path to the current Python interpreter.

    Returns
    -------
    str
        The path to the Python interpreter executable.
    """

    return sys.executable



