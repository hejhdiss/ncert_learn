import os
current_binary_path = ""
def isbinaryfile(file_path):
    """
    Check if a file is a binary file.
    
    Parameters:
    file_path (str): Path to the file.

    Returns:
    bool: True if the file is a binary file, False otherwise.
    """
    try:
        with open(file_path, 'rb') as file:
            file.read(1024)  # Read the first 1024 bytes as a test
        return True
    except (UnicodeDecodeError, IOError):
        return False


def copybinaryfromonetoanother(src, dest):
    """
    Copies the binary content from the file given by path src to the file given by path dest.

    Parameters
    ----------
    src : str
        The path of the file to copy from.
    dest : str
        The path of the file to copy to.

    Returns
    -------
    bool
        True if the copy operation is successful, False otherwise.
    """
    if not isinstance(src, str) or not isinstance(dest, str) or not src or not dest:
        return False
    elif not isbinaryfile(src):
        return False
    try:
        with open(src, 'rb') as file_src:
            with open(dest, 'wb') as file_dest:
                file_dest.write(file_src.read())
        return True
    except (FileNotFoundError, IOError):
        return False


def openbinaryfile(file_path):
    """
    Opens the binary file given by path file_path to set it as the current working file.

    Parameters
    ----------
    file_path : str
        The path of the file to open.

    Returns
    -------
    bool
        True if the file is opened successfully, False otherwise.
    """
    global current_binary_path

    if not isinstance(file_path, str) or not file_path or not isbinaryfile(file_path):
        return False
    try:
        with open(file_path, 'rb') as file:
            current_binary_path = file_path
        return True
    except (FileNotFoundError, IOError):
        return False


def addtextobinaryfile(byte_data):
    """
    Appends a sequence of bytes to the binary file opened by openbinaryfile() function.

    Parameters
    ----------
    byte_data : bytes
        A sequence of bytes to append.

    Returns
    -------
    bool
        True if the bytes are appended successfully, False otherwise.
    """
    global current_binary_path
    if not current_binary_path or not isinstance(byte_data, bytes):
        return False
    try:
        with open(current_binary_path, 'ab') as file:
            file.write(byte_data)
        return True
    except (FileNotFoundError, IOError):
        return False


def readbinaryfile():
    """
    Reads the contents of the binary file opened by openbinaryfile() function.

    Returns
    -------
    bytes
        The contents of the file as bytes.
    """
    global current_binary_path
    try:
        with open(current_binary_path, 'rb') as file:
            return file.read()
    except (FileNotFoundError, IOError):
        return b''


def clearbinaryfile():
    """
    Clears the contents of the binary file opened by openbinaryfile() function.
    """
    global current_binary_path
    if current_binary_path:
        with open(current_binary_path, 'wb') as file:
            pass  # Overwrite with an empty file


def readbinaryspecificchunk(offset, size):
    """
    Reads a specific chunk from the binary file opened by openbinaryfile() function.

    Parameters
    ----------
    offset : int
        The starting position to read from the file.
    size : int
        The number of bytes to read.

    Returns
    -------
    bytes
        The content of the specified chunk as bytes if successful.
    bool
        False if the file is not found or any exception occurs.
    """
    global current_binary_path

    try:
        with open(current_binary_path, 'rb') as file:
            file.seek(offset)
            return file.read(size)
    except (FileNotFoundError, IOError):
        return False


# Initialize current binary path variable

