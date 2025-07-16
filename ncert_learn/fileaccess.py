import os
import requests
from datetime import datetime

def check_file_existence(file_path):
    """
    Checks if a file exists at the given path.

    Args:
        file_path (str): Path to the file.

    Returns:
        bool: True if file exists, False otherwise.
    """
    return os.path.exists(file_path)

def create_directory(dir_path):
    """
    Creates a directory if it doesn't exist.

    Args:
        dir_path (str): Path to the directory.
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def download_file(url, download_path):
    """
    Downloads a file from the given URL and saves it to the specified path.

    Args:
        url (str): URL of the file to download.
        download_path (str): Local path to save the downloaded file.
    
    Returns:
        bool: True if download was successful, False otherwise.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(download_path, 'wb') as file:
            file.write(response.content)
        return True
    except requests.RequestException as e:
        print(f"Error downloading file: {e}")
        return False

def get_file_size(file_path):
    """
    Retrieves the size of a file.

    Args:
        file_path (str): Path to the file.
    
    Returns:
        int: Size of the file in bytes, or -1 if file doesn't exist.
    """
    if os.path.exists(file_path):
        return os.path.getsize(file_path)
    return -1

def get_file_last_modified(file_path):
    """
    Retrieves the last modification date of a file.

    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: Last modification date in 'YYYY-MM-DD HH:MM:SS' format, or 'N/A' if file doesn't exist.
    """
    if os.path.exists(file_path):
        timestamp = os.path.getmtime(file_path)
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    return 'N/A'

def rename_file(old_name, new_name):
    """
    Renames a file.

    Args:
        old_name (str): Current name of the file.
        new_name (str): New name for the file.
    
    Returns:
        bool: True if renaming was successful, False otherwise.
    """
    try:
        os.rename(old_name, new_name)
        return True
    except OSError as e:
        print(f"Error renaming file: {e}")
        return False

def move_file(src_path, dest_path):
    """
    Moves a file to a new location.

    Args:
        src_path (str): Source path of the file.
        dest_path (str): Destination path to move the file.
    
    Returns:
        bool: True if file was moved successfully, False otherwise.
    """
    try:
        os.rename(src_path, dest_path)
        return True
    except OSError as e:
        print(f"Error moving file: {e}")
        return False

def delete_file(file_path):
    """
    Deletes a file.

    Args:
        file_path (str): Path to the file to delete.
    
    Returns:
        bool: True if file was deleted successfully, False otherwise.
    """
    try:
        os.remove(file_path)
        return True
    except OSError as e:
        print(f"Error deleting file: {e}")
        return False

def extract_zip(zip_path, extract_to):
    """
    Extracts the contents of a ZIP file.

    Args:
        zip_path (str): Path to the ZIP file.
        extract_to (str): Destination directory to extract contents to.
    
    Returns:
        bool: True if extraction was successful, False otherwise.
    """
    try:
        import zipfile
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        return True
    except (zipfile.BadZipFile, FileNotFoundError) as e:
        print(f"Error extracting ZIP file: {e}")
        return False

def compress_files(files, zip_name):
    """
    Compresses multiple files into a ZIP archive.

    Args:
        files (list): List of file paths to include in the ZIP.
        zip_name (str): Name of the output ZIP archive.
    
    Returns:
        bool: True if compression was successful, False otherwise.
    """
    try:
        import zipfile
        with zipfile.ZipFile(zip_name, 'w') as zip_ref:
            for file in files:
                zip_ref.write(file, os.path.basename(file))
        return True
    except (FileNotFoundError, zipfile.BadZipFile) as e:
        print(f"Error compressing files: {e}")
        return False

def get_url_status(url):
    """
    Checks the HTTP status of a URL.

    Args:
        url (str): URL to check.

    Returns:
        int: HTTP status code.
    """
    try:
        response = requests.get(url)
        return response.status_code
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return -1

def fetch_url_content(url):
    """
    Fetches the content of a URL.

    Args:
        url (str): URL to fetch content from.

    Returns:
        str: Content of the URL if successful, 'Error' if request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL content: {e}")
        return 'Error'

def download_files_from_urls(url_list, download_dir):
    """
    Downloads multiple files from a list of URLs.

    Args:
        url_list (list): List of URLs to download.
        download_dir (str): Directory to save downloaded files.
    
    Returns:
        list: List of filenames downloaded.
    """
    create_directory(download_dir)
    downloaded_files = []
    for url in url_list:
        filename = os.path.join(download_dir, os.path.basename(url))
        if download_file(url, filename):
            downloaded_files.append(filename)
    return downloaded_files

def get_files_in_directory(directory):
    """
    Retrieves all files in a directory.

    Args:
        directory (str): Directory path.

    Returns:
        list: List of file names in the directory.
    """
    if os.path.exists(directory):
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return []

def count_lines_in_file(file_path):
    """
    Counts the number of lines in a file.

    Args:
        file_path (str): Path to the file.
    
    Returns:
        int: Number of lines in the file, or -1 if file doesn't exist.
    """
    try:
        with open(file_path, 'r') as file:
            return len(file.readlines())
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
        return -1

def get_current_datetime():
    """
    Retrieves the current date and time.

    Returns:
        str: Current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def get_extension(file_name):
    """
    Retrieves the file extension.

    Args:
        file_name (str): Name of the file.
    
    Returns:
        str: File extension (e.g., '.txt').
    """
    return os.path.splitext(file_name)[1]

def get_file_name_without_extension(file_name):
    """
    Retrieves the file name without the extension.

    Args:
        file_name (str): Name of the file.
    
    Returns:
        str: File name without the extension.
    """
    return os.path.splitext(file_name)[0]

def get_file_type(file_path):
    """
    Determines the file type based on its extension.

    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: File type (e.g., 'text', 'image', 'pdf').
    """
    extension = get_extension(file_path)
    if extension in ['.txt', '.md', '.rtf']:
        return 'text'
    elif extension in ['.jpg', '.jpeg', '.png']:
        return 'image'
    elif extension == '.pdf':
        return 'pdf'
    return 'unknown'

def move_files_to_directory(file_list, directory):
    """
    Moves a list of files to a specified directory.

    Args:
        file_list (list): List of file paths to move.
        directory (str): Destination directory.
    
    Returns:
        list: List of successfully moved files.
    """
    create_directory(directory)
    moved_files = []
    for file in file_list:
        destination = os.path.join(directory, os.path.basename(file))
        if move_file(file, destination):
            moved_files.append(destination)
    return moved_files
