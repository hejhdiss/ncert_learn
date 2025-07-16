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
def modifyspecificlinebinary(line_number, new_content):
    """
    Modifies a specific line in the text file.

    Parameters
    ----------
    line_number : int
        The line number to modify (1-based index).
    new_content : str
        The new content to set for the specified line.

    Returns
    -------
    bool
        True if the line was successfully modified, False if there was an error (e.g., file not found or invalid line number).
    """
    global current_text_path

    try:
        with open(current_text_path, 'r') as file:
            lines = file.readlines()

        # Check if the line number is valid
        if line_number <= 0 or line_number > len(lines):
            return False

        # Modify the specified line
        lines[line_number - 1] = new_content + '\n'

        # Write the modified content back to the file
        with open(current_text_path, 'w') as file:
            file.writelines(lines)

        return True
    except (FileNotFoundError, IOError, IndexError):
        return False


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
def overwritebinaryfile(new_data):
    """
    Overwrites the contents of the binary file opened by openbinaryfile() with new data.

    Parameters
    ----------
    new_data : bytes
        The new content to write to the binary file.

    Returns
    -------
    bool
        True if the file is overwritten successfully, False otherwise.
    """
    global current_binary_path

    if not current_binary_path or not isinstance(new_data, bytes):
        return False
    try:
        with open(current_binary_path, 'wb') as file:
            file.write(new_data)
        return True
    except (FileNotFoundError, IOError):
        return False
import os

def binary_file_operations_advanced_mode(folder_path, operation, file_name=None, new_name=None, data=None):
    """
    Perform various binary file operations in a specified folder.

    Parameters
    ----------
    folder_path : str
        Path to the folder where the operations will be performed.
    operation : str
        The operation to perform. Supported operations:
        'create', 'write', 'append', 'read', 'clear', 'delete', 'rename', 'list_files'.
    file_name : str, optional
        The file name for the operation.
    new_name : str, optional
        New name for the file (used in 'rename').
    data : bytes, optional
        Binary data for 'write' or 'append' operations.

    Returns
    -------
    bool or bytes or list
        - For 'read': Returns file content (bytes) or False on error.
        - For 'list_files': Returns a list of files in the folder or False on error.
        - For other operations: Returns True on success, False on failure.
    """
    # Check if the folder path is valid
    if not folder_path or not os.path.isdir(folder_path):
        return False

    try:
        file_path = os.path.join(folder_path, file_name) if file_name else None

        # Create a new binary file
        if operation == 'create':
            if not file_name:
                return False
            with open(file_path, 'wb') as file:
                pass  # Create an empty binary file
            return True

        # Write binary data to a file
        elif operation == 'write':
            if not file_name or data is None or not isinstance(data, bytes):
                return False
            with open(file_path, 'wb') as file:
                file.write(data)
            return True

        # Append binary data to a file
        elif operation == 'append':
            if not file_name or data is None or not isinstance(data, bytes):
                return False
            with open(file_path, 'ab') as file:
                file.write(data)
            return True

        # Read binary file content
        elif operation == 'read':
            if not file_name:
                return False
            with open(file_path, 'rb') as file:
                return file.read()

        # Clear binary file content
        elif operation == 'clear':
            if not file_name:
                return False
            with open(file_path, 'wb') as file:
                pass  # Overwrite with an empty binary file
            return True

        # Delete a binary file
        elif operation == 'delete':
            if not file_name:
                return False
            os.remove(file_path)
            return True

        # Rename a binary file
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

    except (FileNotFoundError, PermissionError, OSError):
        return False

