import subprocess
import sys

def execute_command(cmd):
    """
    Execute a shell command and return the output.

    Args:
        cmd (str): The command to execute

    Returns:
        tuple: A tuple of (success, output/error message)
    """
    try:
        # Run the command and capture the output and error messages
        result = subprocess.run(cmd, shell=True, check=True, text=True, capture_output=True)
        # If the command is successful, return the output
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        # If there is an error, return False and the error message
        return False, e.stderr
    except Exception as e:
        # Catch any other exceptions and return them
        return False, str(e)


# Function to list files in a directory (Windows version)
def cmd_list_files(directory="."):
    """
    List files in a directory.

    Args:
        directory (str): The directory to list files from (default is current directory)

    Returns:
        tuple: A tuple of (success, list of files or error message)
    """
    cmd = f"dir {directory}"
    return execute_command(cmd)


# Function to get disk usage (Windows version)
def cmd_get_disk_usage():
    """
    Get disk usage statistics.

    Returns:
        tuple: A tuple of (success, disk usage information or error message)
    """
    cmd = "wmic logicaldisk get size,freespace,caption"
    return execute_command(cmd)


# Function to check the system's memory usage (Windows version)
def cmd_get_memory_usage():
    """
    Get memory usage statistics.

    Returns:
        tuple: A tuple of (success, memory usage information or error message)
    """
    cmd = "systeminfo | findstr /C:\"Total Physical Memory\" /C:\"Available Physical Memory\""
    return execute_command(cmd)


# Function to check running processes (Windows version)
def cmd_get_running_processes():
    """
    Get the list of currently running processes.

    Returns:
        tuple: A tuple of (success, list of processes or error message)
    """
    cmd = "tasklist"
    return execute_command(cmd)


# Function to kill a process by its PID (Windows version)
def cmd_kill_process(pid):
    """
    Kill a process by its PID.

    Args:
        pid (str): The process ID to kill

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = f"taskkill /PID {pid} /F"
    return execute_command(cmd)


# Function to create a new directory (Windows version)
def cmd_create_directory(directory):
    """
    Create a new directory.

    Args:
        directory (str): The name of the directory to create

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = f"mkdir {directory}"
    return execute_command(cmd)


# Function to delete a file or directory (Windows version)
def cmd_delete_file_or_directory(path):
    """
    Delete a file or directory.

    Args:
        path (str): The path of the file or directory to delete

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = f"del /f /s /q {path} || rmdir /s /q {path}"
    return execute_command(cmd)


# Function to check the system uptime (Windows version)
def cmd_get_system_uptime():
    """
    Get the system uptime.

    Returns:
        tuple: A tuple of (success, system uptime or error message)
    """
    cmd = "systeminfo | findstr /C:\"System Boot Time\""
    return execute_command(cmd)


# Function to check the system's kernel version (Windows version)
def cmd_get_kernel_version():
    """
    Get the system's kernel version.

    Returns:
        tuple: A tuple of (success, kernel version or error message)
    """
    cmd = "ver"
    return execute_command(cmd)


# Function to check system load (Windows version)
def cmd_get_system_load():
    """
    Get the system's load averages.

    Returns:
        tuple: A tuple of (success, load averages or error message)
    """
    cmd = "wmic cpu get loadpercentage"
    return execute_command(cmd)


# Function to check for available software updates (Windows version)
def cmd_check_for_updates():
    """
    Check if there are any available software updates.

    Returns:
        tuple: A tuple of (success, update information or error message)
    """
    cmd = "powershell -Command \"Get-WindowsUpdate\""
    return execute_command(cmd)


# Function to install a package (Windows version)
def cmd_install_package(package_name):
    """
    Install a package using Windows package manager (e.g., Chocolatey or Winget).

    Args:
        package_name (str): The name of the package to install

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = f"winget install {package_name}"
    return execute_command(cmd)


# Function to uninstall a package (Windows version)
def cmd_uninstall_package(package_name):
    """
    Uninstall a package using Windows package manager (e.g., Chocolatey or Winget).

    Args:
        package_name (str): The name of the package to uninstall

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = f"winget uninstall {package_name}"
    return execute_command(cmd)


# Function to check active user sessions (Windows version)
def cmd_get_active_users():
    """
    Get active user sessions on the system.

    Returns:
        tuple: A tuple of (success, active users or error message)
    """
    cmd = "query user"
    return execute_command(cmd)


# Function to get the IP address of the system (Windows version)
def cmd_get_ip_address():
    """
    Get the system's IP address.

    Returns:
        tuple: A tuple of (success, IP address or error message)
    """
    cmd = "ipconfig"
    return execute_command(cmd)


# Function to check firewall status (Windows version)
def cmd_check_firewall_status():
    """
    Check the status of the system's firewall.

    Returns:
        tuple: A tuple of (success, firewall status or error message)
    """
    cmd = "netsh advfirewall show allprofiles"
    return execute_command(cmd)


# Function to flush DNS cache (Windows version)
def cmd_flush_dns_cache():
    """
    Flush the DNS cache.

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = "ipconfig /flushdns"
    return execute_command(cmd)


# Function to check system temperature (Windows version)
def cmd_get_system_temperature():
    """
    Get system temperature (may require third-party tools like OpenHardwareMonitor).

    Returns:
        tuple: A tuple of (success, temperature or error message)
    """
    cmd = "wmic /namespace:\\\\root\\wmi PATH MSAcpi_ThermalZoneTemperature get CurrentTemperature"
    return execute_command(cmd)


# Function to reset TCP/IP stack (Windows version)
def cmd_reset_tcpip_stack():
    """
    Reset TCP/IP stack settings.

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = "netsh int ip reset"
    return execute_command(cmd)


# Function to check for disk errors (Windows version)
def cmd_check_disk_for_errors(drive="C:"):
    """
    Check a disk for errors (requires admin privileges).

    Args:
        drive (str): The drive to check (default is C:)

    Returns:
        tuple: A tuple of (success, disk check results or error message)
    """
    cmd = f"chkdsk {drive}"
    return execute_command(cmd)


# Function to restart the system (Windows version)
def cmd_restart_system():
    """
    Restart the system.

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = "shutdown /r /f /t 0"
    return execute_command(cmd)


# Function to shut down the system (Windows version)
def cmd_shutdown_system():
    """
    Shut down the system.

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = "shutdown /s /f /t 0"
    return execute_command(cmd)


# Function to open Control Panel (Windows version)
def cmd_open_control_panel():
    """
    Open the Control Panel.

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = "control"
    return execute_command(cmd)


# Function to open the Task Manager (Windows version)
def cmd_open_task_manager():
    """
    Open the Task Manager.

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = "taskmgr"
    return execute_command(cmd)


# Function to check Windows services (Windows version)
def cmd_check_services():
    """
    Get the list of active Windows services.

    Returns:
        tuple: A tuple of (success, active services or error message)
    """
    cmd = "sc query"
    return execute_command(cmd)


# Function to start a service (Windows version)
def cmd_start_service(service_name):
    """
    Start a Windows service.

    Args:
        service_name (str): The name of the service to start

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = f"sc start {service_name}"
    return execute_command(cmd)


# Function to stop a service (Windows version)
def cmd_stop_service(service_name):
    """
    Stop a Windows service.

    Args:
        service_name (str): The name of the service to stop

    Returns:
        tuple: A tuple of (success, message or error message)
    """
    cmd = f"sc stop {service_name}"
    return execute_command(cmd)


# Function to view system environment variables (Windows version)
def cmd_view_env_variables():
    """
    View system environment variables.

    Returns:
        tuple: A tuple of (success, environment variables or error message)
    """
    cmd = "set"
    return execute_command(cmd)
