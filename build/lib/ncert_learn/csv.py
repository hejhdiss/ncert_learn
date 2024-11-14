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


# Initialize current CSV path variable


