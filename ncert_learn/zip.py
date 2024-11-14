import zipfile
import os

SUPPORTED_EXTENSIONS = {'.zip', '.txt', '.csv', '.json'}

def zip_is_supported_file(file_path):
    """Checks if the given file has a supported extension.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file has a supported extension, False otherwise.
    """
    _, extension = os.path.splitext(file_path)
    return extension in SUPPORTED_EXTENSIONS

def zip_is_supported(zip_path):
    """Checks if the given ZIP file is supported (i.e., if it's a valid ZIP file).

    Args:
        zip_path (str): The path to the ZIP file.

    Returns:
        bool: True if the file is a valid ZIP file, False otherwise.
    """
    return os.path.exists(zip_path) and zipfile.is_zipfile(zip_path)

def zip_list_files(zip_path):
    """Returns a list of all files within the given ZIP archive.

    Args:
        zip_path (str): The path to the ZIP archive.

    Returns:
        list[str]: A list of the names of all files in the ZIP archive, or False if the path is invalid, or the file is not a ZIP archive.
    """
    if not zip_is_supported(zip_path):
        return False

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            return zip_file.namelist()
    except zipfile.BadZipFile:
        return False

def zip_extract_file(zip_path, file_name, destination="."):
    """Extract a specific file from the ZIP archive to a destination directory.

    Args:
        zip_path (str): The path to the ZIP archive.
        file_name (str): The name of the file to extract.
        destination (str): The directory to extract the file to. Default is the current directory.

    Returns:
        bool: True if the file was extracted successfully, False otherwise.
    """
    if not zip_is_supported(zip_path):
        return False

    if not zip_is_supported_file(file_name):
        return False

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            if file_name in zip_file.namelist():
                zip_file.extract(file_name, destination)
                return True
            return False
    except (FileNotFoundError, zipfile.BadZipFile):
        return False

def zip_add_file(zip_path, file_path):
    """Add a file to the ZIP archive.

    Args:
        zip_path (str): The path to the ZIP archive.
        file_path (str): The path to the file to add.

    Returns:
        bool: True if the file was added successfully, False otherwise.
    """
    if not zip_is_supported(zip_path):
        return False

    if not os.path.exists(file_path) or not zip_is_supported_file(file_path):
        return False

    try:
        with zipfile.ZipFile(zip_path, 'a') as zip_file:
            zip_file.write(file_path, arcname=os.path.basename(file_path))
            return True
    except zipfile.BadZipFile:
        return False

def zip_extract_all(zip_path, destination="."):
    """Extract all files from the ZIP archive to the given destination.

    Args:
        zip_path (str): The path to the ZIP archive.
        destination (str): The directory path where the files will be extracted. Default is ".".

    Returns:
        bool: True if all files were successfully extracted, False otherwise.
    """
    if not zip_is_supported(zip_path):
        return False

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            zip_file.extractall(destination)
            return True
    except (FileNotFoundError, zipfile.BadZipFile):
        return False

