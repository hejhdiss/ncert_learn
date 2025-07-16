import os
import subprocess
import sys
import ctypes
import time

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return os.geteuid() == 0
    except AttributeError:
        # Windows check
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def install_nmap(installer_path):
    """Install nmap using the Windows installer with elevated privileges."""
    try:
        print("Installing nmap...")
        # Correctly quote the installer path for PowerShell to handle spaces
        installer_path = f'"{installer_path}"'  # Enclose the path in quotes
        # Using Start-Process to run the installer with elevated privileges
        subprocess.check_call([
            'powershell', 
            'Start-Process', 
            installer_path, 
            '-ArgumentList', '/S',  # Silent install
            '-Verb', 'RunAs'
        ])
        print("nmap installation completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install nmap. Error: {e}")
        return False
    return True

def download_installer():
    """Download the nmap installer."""
    nmap_installer_url = 'https://nmap.org/dist/nmap-7.93-setup.exe'
    installer_path = os.path.join(os.getcwd(), 'nmap-setup.exe')

    try:
        print(f"Downloading nmap installer from {nmap_installer_url}...")
        subprocess.check_call(['curl', '-o', installer_path, nmap_installer_url])
        print(f"Installer downloaded to {installer_path}.")
        return installer_path
    except subprocess.CalledProcessError as e:
        print(f"Error downloading the installer: {e}")
        return None

def delete_installer(installer_path):
    """Delete the downloaded installer file."""
    try:
        # Adding a slight delay to ensure the installer is completely done before trying to delete
        time.sleep(2)  # Sleep for 2 seconds

        if os.path.exists(installer_path):
            os.remove(installer_path)
            print(f"Deleted the installer file: {installer_path}")
        else:
            print(f"Installer file does not exist: {installer_path}")
    except Exception as e:
        print(f"Failed to delete the installer file. Error: {e}")

def run_as_admin():
    """Request for administrator privileges."""
    try:
        print("This script requires administrator privileges. Requesting admin privileges...")
        
        # Correctly quote the Python executable and script path
        python_path = sys.executable
        script_path = sys.argv[0]
        command = f'"{python_path}" "{script_path}"'
        
        # Use PowerShell's Start-Process to run the script as administrator
        subprocess.check_call([
            'powershell', 
            '-Command', 
            f'Start-Process "{python_path}" -ArgumentList "{script_path}" -Verb RunAs'
        ])
    except subprocess.CalledProcessError as e:
        print(f"Failed to request admin privileges: {e}")
        sys.exit(1)

def install_and_setup_nmap():
    """Main function to handle the installation."""
    # Check if the script is running as admin
    if not is_admin():
        print("Script is not running with administrator privileges.")
        # Request admin privileges to run the script again
        run_as_admin()
    
    # If script is already running as admin, proceed with the installation
    print("Running with administrator privileges. Continuing with installation...")
    installer_path = download_installer()
    if installer_path:
        if install_nmap(installer_path):
            print("nmap installation completed successfully.")
            # Delete the installer after installation
            delete_installer(installer_path)


