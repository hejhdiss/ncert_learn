import os
import subprocess
import logging
import webbrowser
import time
import psutil
import requests

# Set up logging for better tracking and diagnostics
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def check_xampp_files(xampp_path="C:\\xampp"):
    """
    Checks if the necessary XAMPP files are present in the given directory (default is C:\\xampp).
    Returns True if all required files exist; otherwise, False.
    
    Args:
    - xampp_path (str): The directory path where XAMPP is installed. Default is "C:\\xampp".
    """
    required_files = [
        os.path.join(xampp_path, "mysql\\bin\\mysqld.exe"),
        os.path.join(xampp_path, "apache\\bin\\httpd.exe"),
        os.path.join(xampp_path, "phpMyAdmin")
    ]
    
    for file in required_files:
        if not os.path.exists(file):
            logging.error(f"Missing file: {file}")
            return False  # File is missing
    
    logging.info("XAMPP files are present.")
    return True  # All required files are found
def is_process_running_xampp(process_name):
    """
    Checks if a given process is currently running using psutil.
    
    Args:
    - process_name (str): The name of the process to check (e.g., "mysqld" for MySQL, "httpd" for Apache).
    
    Returns:
    - bool: True if the process is running, False otherwise.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

def is_process_running(process_name):
    """
    Check if a process is running by its name.
    
    Args:
    - process_name (str): The name of the process to check.
    
    Returns:
    - bool: True if the process is running, False otherwise.
    """
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            return True
    return False

def stop_xampp_mysql(xampp_path="C:\\xampp"):
    """
    Stops the MySQL server of XAMPP if it is running.
    
    Args:
    - xampp_path (str): The directory path where XAMPP is installed. Default is "C:\\xampp".
    """
    if is_process_running("mysqld.exe"):
        mysql_pid = None
        # Iterate through processes and find the specific MySQL process used by XAMPP
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                # Check if the process is mysqld.exe and belongs to XAMPP directory
                if "mysqld.exe" in proc.info['name'].lower() and xampp_path.lower() in proc.info['exe'].lower():
                    mysql_pid = proc.info['pid']
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle process access errors or already terminated processes
                pass
        
        if mysql_pid:
            try:
                p = psutil.Process(mysql_pid)
                p.terminate()
                logging.info("XAMPP MySQL server stopped successfully.")
            except Exception as e:
                logging.error(f"Failed to stop XAMPP MySQL server: {e}")
        else:
            logging.warning("XAMPP MySQL server process not found.")
    else:
        logging.info("XAMPP MySQL service is not running.")
def stop_xampp_apache(xampp_path="C:\\xampp"):
    """
    Stops the Apache server of XAMPP if it is running.
    
    Args:
    - xampp_path (str): The directory path where XAMPP is installed. Default is "C:\\xampp".
    """
    if is_process_running("httpd.exe"):
        apache_pid = None
        # Iterate through processes and find the specific Apache process used by XAMPP
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                # Check if the process is httpd.exe and belongs to XAMPP directory
                if "httpd.exe" in proc.info['name'].lower() and xampp_path.lower() in proc.info['exe'].lower():
                    apache_pid = proc.info['pid']
                    break
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle process access errors or already terminated processes
                pass
        
        if apache_pid:
            try:
                p = psutil.Process(apache_pid)
                p.terminate()
                logging.info("XAMPP Apache server stopped successfully.")
            except Exception as e:
                logging.error(f"Failed to stop XAMPP Apache server: {e}")
        else:
            logging.warning("XAMPP Apache server process not found.")
    else:
        logging.info("XAMPP Apache service is not running.")

def start_xampp_mysql(xampp_path="C:\\xampp"):
    """
    Starts the MySQL server of XAMPP if it is not already running.
    
    Args:
    - xampp_path (str): The directory path where XAMPP is installed. Default is "C:\\xampp".
    """
    if not check_xampp_files(xampp_path):
        logging.error("XAMPP configuration is incorrect or files are missing.")
        return False

    # Start MySQL if it's not already running
    if not is_process_running("mysqld"):
        mysql_command = [os.path.join(xampp_path, 'mysql\\bin\\mysqld.exe')]
        try:
            subprocess.Popen(mysql_command)
            logging.info("XAMPP MySQL server started successfully.")
            return True
        except Exception as e:
            logging.error(f"Failed to start MySQL: {e}")
            return False
    logging.info("MySQL is already running.")
    return True  # MySQL is already running

def start_xampp_apache(xampp_path="C:\\xampp"):
    """
    Starts the Apache server of XAMPP if it is not already running.
    
    Args:
    - xampp_path (str): The directory path where XAMPP is installed. Default is "C:\\xampp".
    """
    if not check_xampp_files(xampp_path):
        logging.error("XAMPP configuration is incorrect or files are missing.")
        return False

    # Start Apache if it's not already running
    if not is_process_running("httpd"):
        apache_command = [os.path.join(xampp_path, 'apache\\bin\\httpd.exe')]
        try:
            subprocess.Popen(apache_command)
            logging.info("XAMPP Apache server started successfully.")
            return True
        except Exception as e:
            logging.error(f"Failed to start Apache: {e}")
            return False
    logging.info("Apache is already running.")
    return True  # Apache is already running
def check_phpmyadmin_accessible(url="http://localhost/phpmyadmin"):
    """
    Check if phpMyAdmin is accessible via the provided URL.
    
    Args:
    - url (str): The URL of phpMyAdmin (default is "http://localhost/phpmyadmin").
    
    Returns:
    - bool: True if phpMyAdmin is accessible, False otherwise.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info("phpMyAdmin is accessible.")
            return True
        else:
            logging.error(f"phpMyAdmin returned status code: {response.status_code}")
            return False
    except requests.RequestException as e:
        logging.error(f"Error checking phpMyAdmin: {e}")
        return False

def start_xampp_and_open_phpmyadmin(xampp_path="C:\\xampp"):
    """
    Starts MySQL and Apache servers, and then opens phpMyAdmin in the web browser.
    
    Args:
    - xampp_path (str): The directory path where XAMPP is installed. Default is "C:\\xampp".
    """
    # Check if XAMPP files exist
    if not check_xampp_files(xampp_path):
        logging.error("XAMPP configuration is incorrect or files are missing.")
        return False

    # Stop MySQL and Apache if they are running and restart them
    stop_xampp_mysql(xampp_path)
    stop_xampp_apache(xampp_path)
    
    # Start MySQL and Apache servers
    mysql_started = start_xampp_mysql(xampp_path)
    apache_started = start_xampp_apache(xampp_path)
    
    if mysql_started and apache_started:
        logging.info("Both MySQL and Apache started successfully.")
        
        # Open phpMyAdmin in the default web browser
        try:
            # Ensure a short delay for servers to start
            time.sleep(5)  # Wait for MySQL and Apache to fully start
            webbrowser.open("http://localhost/phpmyadmin")
            logging.info("phpMyAdmin opened successfully in the web browser.")
            
            # Check if phpMyAdmin is accessible
            if check_phpmyadmin_accessible():
                return True  # Successfully opened phpMyAdmin
            else:
                return False  # phpMyAdmin is not accessible
        except Exception as e:
            logging.error(f"Error opening phpMyAdmin: {e}")
            return False  # Error opening phpMyAdmin
    else:
        logging.error("Failed to start MySQL and Apache.")
        return False  # Failure to start MySQL or Apache

# Example usage of the function


