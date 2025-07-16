import os
import csv
current_csv_path = ""

def iscsvfile(file_path):
    """
    Check if a file is a CSV file.
    
    Parameters:
    file_path (str): Path to the file.

    Returns:
    bool: True if the file is a CSV file, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv.reader(file)  # Try reading as CSV
        return True
    except (csv.Error, UnicodeDecodeError, IOError):
        return False


def copycsvfromonetoanother(src, dest):
    """
    Copies the CSV content from the file given by path src to the file given by path dest.

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
    elif not iscsvfile(src) or not iscsvfile(dest):
        return False
    try:
        with open(src, 'r', newline='', encoding='utf-8') as file_src:
            reader = csv.reader(file_src)
            with open(dest, 'w', newline='', encoding='utf-8') as file_dest:
                writer = csv.writer(file_dest)
                for row in reader:
                    writer.writerow(row)
        return True
    except (FileNotFoundError, IOError, csv.Error):
        return False


def opencsvfile(file_path):
    """
    Opens the CSV file given by path file_path to set it as the current working file.

    Parameters
    ----------
    file_path : str
        The path of the file to open.

    Returns
    -------
    bool
        True if the file is opened successfully, False otherwise.
    """
    global current_csv_path

    if not isinstance(file_path, str) or not file_path or not iscsvfile(file_path):
        return False
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            current_csv_path = file_path
        return True
    except (FileNotFoundError, IOError):
        return False


def addrowtocsv(row_data):
    """
    Appends a row of data to the CSV file opened by opencsvfile() function.

    Parameters
    ----------
    row_data : list
        A list of values representing a row to append.

    Returns
    -------
    bool
        True if the row is appended successfully, False otherwise.
    """
    global current_csv_path
    if not current_csv_path or not isinstance(row_data, list):
        return False
    try:
        with open(current_csv_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(row_data)
        return True
    except (FileNotFoundError, IOError, csv.Error):
        return False


def readcsvfile():
    """
    Reads the contents of the CSV file opened by opencsvfile() function.

    Returns
    -------
    list
        A list of rows, where each row is a list of column values.
    """
    global current_csv_path
    try:
        with open(current_csv_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            return list(reader)
    except (FileNotFoundError, IOError, csv.Error):
        return []


def clearcsvfile():
    """
    Clears the contents of the CSV file opened by opencsvfile() function.
    """
    global current_csv_path
    if current_csv_path:
        with open(current_csv_path, 'w', newline='', encoding='utf-8') as file:
            pass  # Overwrite with an empty file


def readcsvspecificline(line_number):
    """
    Reads a specific line from the CSV file opened by opencsvfile() function.

    Parameters
    ----------
    line_number : int
        The line number to read from the file (1-based index).

    Returns
    -------
    list
        The content of the specified line as a list if successful.
    bool
        False if the line number is out of range or any other exception occurs.
    """
    global current_csv_path

    try:
        with open(current_csv_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if line_number <= 0 or line_number > len(rows):
                return False
            return rows[line_number - 1]
    except (FileNotFoundError, csv.Error, IndexError):
        return False
import csv

def modifycsvspecificline(line_number, new_content):
    """
    Modifies a specific line in the CSV file opened by opencsvfile() function.

    Parameters
    ----------
    line_number : int
        The line number to modify (1-based index).
    new_content : list
        The new content to replace the specified line with (as a list of values).

    Returns
    -------
    bool
        True if the line was successfully modified, False if the file is not found, line number is out of range, or any other exception occurs.
    """
    global current_csv_path

    try:
        # Read the current content of the CSV file
        with open(current_csv_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Check if the line number is within the valid range
        if line_number <= 0 or line_number > len(rows):
            return False

        # Modify the specified line
        rows[line_number - 1] = new_content  # Replace the line with the new content

        # Write the modified content back to the CSV file
        with open(current_csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        return True
    except (FileNotFoundError, csv.Error, IndexError):
        return False
    except Exception:
        return False





# Initialize current CSV path variable
def overwritecsvfile(rows):
    """
    Overwrites the contents of the CSV file opened by opencsvfile() function.

    Parameters
    ----------
    rows : list
        A list of rows, where each row is a list of column values.

    Returns
    -------
    bool
        True if the file is overwritten successfully, False otherwise.
    """
    global current_csv_path

    if not current_csv_path or not isinstance(rows, list) or not all(isinstance(row, list) for row in rows):
        return False
    try:
        with open(current_csv_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        return True
    except (FileNotFoundError, IOError, csv.Error):
        return False
import os
import csv

def csv_file_operations_advanced_mode(folder_path, operation, file_name=None, new_name=None, data=None):
    """
    Perform various CSV file operations in a specified folder.

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
    data : list, optional
        Data for 'write' or 'append' operations (list of rows).

    Returns
    -------
    bool or list
        - For 'read': Returns file content (list of rows) or False on error.
        - For 'list_files': Returns a list of files in the folder or False on error.
        - For other operations: Returns True on success, False on failure.
    """
    # Check if the folder path is valid
    if not folder_path or not os.path.isdir(folder_path):
        return False

    try:
        file_path = os.path.join(folder_path, file_name) if file_name else None

        # Create a new CSV file
        if operation == 'create':
            if not file_name or not file_name.endswith('.csv'):
                return False
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                pass  # Create an empty CSV file
            return True

        # Write data to a CSV file (overwrites existing content)
        elif operation == 'write':
            if not file_name or not file_name.endswith('.csv') or not isinstance(data, list):
                return False
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return True

        # Append data to a CSV file
        elif operation == 'append':
            if not file_name or not file_name.endswith('.csv') or not isinstance(data, list):
                return False
            with open(file_path, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(data)
            return True

        # Read a CSV file
        elif operation == 'read':
            if not file_name or not file_name.endswith('.csv'):
                return False
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                return list(reader)

        # Clear a CSV file
        elif operation == 'clear':
            if not file_name or not file_name.endswith('.csv'):
                return False
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                pass  # Overwrite with an empty CSV file
            return True

        # Delete a CSV file
        elif operation == 'delete':
            if not file_name or not file_name.endswith('.csv'):
                return False
            os.remove(file_path)
            return True

        # Rename a CSV file
        elif operation == 'rename':
            if not file_name or not new_name or not file_name.endswith('.csv') or not new_name.endswith('.csv'):
                return False
            new_file_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_file_path)
            return True

        # List all CSV files in the folder
        elif operation == 'list_files':
            return [f for f in os.listdir(folder_path) if f.endswith('.csv')]

        else:
            return False  # Unsupported operation

    except (FileNotFoundError, PermissionError, OSError, csv.Error):
        return False


