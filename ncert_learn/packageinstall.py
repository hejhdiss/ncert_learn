import subprocess
import sys
s=sys.executable



def install_librariesfromlist(libraries):

    """
    Installs the given list of libraries using pip.

    Parameters
    ----------
    libraries : list
        A list of library names to install.

    Returns
    -------
    bool
        True if all libraries are installed successfully, False otherwise.
    """

    if not('list' in str(type(libraries))):
        return False
    elif libraries==[]:
        return False
    else:
        for lib in libraries:
            if not('str' in str(type(lib))):
                pass
            if lib=='':
                pass
            else:
                try:
                    print(f"Installing {lib}...")
                    subprocess.run([s, "-m", "pip", "install", lib], check=True)
                    print(f"{lib} installed successfully.")
                except subprocess.CalledProcessError:
                    print(f"Failed to install {lib}. Please check for errors.")
        return True
def install_library(a):

    """
    Installs the specified library using pip.

    Parameters
    ----------
    a : str
        The name of the library to install.

    Returns
    -------
    bool
        True if the library is installed successfully, False otherwise.
    """

    if not('str' in str(type(a))):
        return False
    elif a=='':
        return False
    else:
        try:
            print(f"Installing {a}...")
            subprocess.run([s, "-m", "pip", "install", a], check=True)
            print(f"{a} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {a}. Please check for errors.")
            return False
        else:
            return True