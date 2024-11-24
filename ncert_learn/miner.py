import subprocess
import os
def get_mining_pool_info_monero():
    """
    Prints information about popular Monero mining pools, including pool names and ports.
    
    Returns:
        None
    """
    mining_pools = {
        "MineXMR": {
            "url": "rx.unmineable.com",
            "ports": ["3333", "443"]
        },
        "SupportXMR": {
            "url": "pool.supportxmr.com",
            "ports": ["3333", "443"]
        },
        "F2Pool": {
            "url": "monero.f2pool.com",
            "ports": ["13531", "13532"]
        },
        "MoneroOcean": {
            "url": "pool.moneroocean.stream",
            "ports": ["10128", "10129"]
        },
        "NanoPool": {
            "url": "xmr-eu1.nanopool.org",
            "ports": ["14444", "14443"]
        },
        "XMRigPool": {
            "url": "xmrpool.eu",
            "ports": ["3333", "443"]
        },
        "Poolin": {
            "url": "xmr.poolin.com",
            "ports": ["8888", "443"]
        }
    }

    print("Monero Mining Pools and Ports:")
    for pool_name, pool_info in mining_pools.items():
        print(f"{pool_name}:")
        print(f"  URL: {pool_info['url']}")
        print(f"  Ports: {', '.join(pool_info['ports'])}")
        print("-" * 40)

def setup_miner_xmrg(wallet_address, pool_url, threads=4):
    """
    Sets up and starts the Monero mining process using XMRig, dynamically locating the executable.
    
    Args:
        wallet_address (str): Your Monero wallet address.
        pool_url (str): Mining pool URL (e.g., "pool.supportxmr.com:3333").
        threads (int): Number of CPU threads to use.
    
    Returns:
        subprocess.Popen: Process handle for the mining process.
    """
    # Dynamically locate the XMRig executable inside the 'xmrig' folder
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Python script
    xmrig_path = os.path.join(script_dir, "xmrig", "xmrig.exe")# Path to the XMRig executable
    
    # Check if XMRig is installed
    if not os.path.exists(xmrig_path):
        raise FileNotFoundError(f"XMRig not found at {xmrig_path}. Ensure it's in the 'xmrig' folder.")
    
    # Build the XMRig command
    command = [
        xmrig_path,
        "-o", pool_url,
        "-u", wallet_address,
        "-p", "x",  # Default password
        "-t", str(threads),  # Number of CPU threads
        "--donate-level=0",
        "--keepalive"# Optional: Set donation level to 1%
    ]

    # Start the miner
    print("Starting the mining process...")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def monitor_miner_monero(process):
    """
    Monitors the output of the mining process.
    
    Args:
        process (subprocess.Popen): The mining process.
    
    Returns:
        None
    """
    try:
        while True:
            output = process.stdout.readline()
            if output:
                print(output.decode().strip())
            else:
                break
    except KeyboardInterrupt:
        print("Stopping the mining process...")
        process.terminate()

def calculate_profitability_monero(hashrate, power_cost, power_consumption):
    """
    Calculates profitability based on hashrate and power costs.
    
    Args:
        hashrate (float): Mining hashrate in H/s.
        power_cost (float): Electricity cost per kWh.
        power_consumption (float): Power consumption in watts.
    
    Returns:
        float: Estimated profitability in USD per day.
    """
    # Example constants (can be updated with live data)
    coin_reward_per_hash = 0.000000012  # Monero reward per hash in USD
    hours_per_day = 24

    # Calculate daily earnings
    daily_earnings = hashrate * coin_reward_per_hash * hours_per_day

    # Calculate daily power cost
    daily_power_cost = (power_consumption / 1000) * power_cost * hours_per_day

    # Calculate net profitability
    return daily_earnings - daily_power_cost

# Example usage
def mine_monero():
    # User inputs
    """
    Initiates Monero mining by setting up a miner and monitoring its output.

    This function collects user inputs for the Monero wallet address, mining pool URL,
    and the number of CPU threads to use. It then starts the mining process using these
    inputs and monitors the output from the mining process. If an error occurs during
    monitoring, it terminates the miner process.

    Returns:
        None
    """

    wallet = input("Enter your Monero wallet address: ")
    pool = input("Enter your mining pool URL (e.g., pool.supportxmr.com:3333): ")
    threads = int(input("Enter the number of CPU threads to use: "))

    # Start mining
    miner_process = setup_miner_xmrg(wallet, pool, threads)

    # Monitor mining output
    try:
        monitor_miner_monero(miner_process)
    except Exception as e:
        print(f"An error occurred: {e}")
        miner_process.terminate()
from cryptography.fernet import Fernet

# Encryption setup
def generate_key():
    """Generates and saves a key for encryption."""
    return Fernet.generate_key()

def load_key():
    """Loads the existing encryption key."""
    return open("secret.key", "rb").read()

def encrypt_wallet(wallet_address, key):
    """Encrypts the wallet address."""
    f = Fernet(key)
    encrypted_wallet = f.encrypt(wallet_address.encode())
    return encrypted_wallet

def decrypt_wallet(encrypted_wallet, key):
    """Decrypts the wallet address."""
    f = Fernet(key)
    decrypted_wallet = f.decrypt(encrypted_wallet).decode()
    return decrypted_wallet
def mine_monero_wallet_saved():
    """
    Initiates Monero mining by setting up a miner and monitoring its output.

    Collects user inputs for the Monero wallet address, mining pool URL,
    and number of CPU threads to use. Starts the mining process using these inputs
    and monitors the output. Optionally, the user can change the wallet address during
    the mining process. The wallet address is saved in an encrypted format.
    """
    # Load or generate encryption key
    if not os.path.exists("secret.key"):
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        key = load_key()

    # Check if an encrypted wallet exists and load it
    wallet_file = "wallet_address.enc"
    if os.path.exists(wallet_file):
        with open(wallet_file, "rb") as file:
            encrypted_wallet = file.read()
        wallet = decrypt_wallet(encrypted_wallet, key)
        print(f"Loaded saved wallet address: {wallet}")
    else:
        wallet = input("Enter your Monero wallet address: ")
        encrypted_wallet = encrypt_wallet(wallet, key)
        with open(wallet_file, "wb") as file:
            file.write(encrypted_wallet)
        print(f"Wallet address saved encrypted to {wallet_file}")

    # Option to change wallet address before mining
    change_wallet = input("Do you want to change the wallet address? (yes/no): ").strip().lower()
    if change_wallet == "yes":
        wallet = input("Enter new Monero wallet address: ")
        encrypted_wallet = encrypt_wallet(wallet, key)
        with open(wallet_file, "wb") as file:
            file.write(encrypted_wallet)
        print("Wallet address updated.")

    # Get pool and thread information
    pool = input("Enter your mining pool URL (e.g., pool.supportxmr.com:3333): ")
    threads = int(input("Enter the number of CPU threads to use: "))

    # Start mining
    miner_process = setup_miner_xmrg(wallet, pool, threads)

    # Monitor mining output
    try:
        monitor_miner_monero(miner_process)
    except Exception as e:
        print(f"An error occurred: {e}")
        miner_process.terminate()

    # Option to change wallet address during mining
    change_wallet = input("Do you want to change the wallet address during mining? (yes/no): ").strip().lower()
    if change_wallet == "yes":
        new_wallet = input("Enter new Monero wallet address: ")
        encrypted_wallet = encrypt_wallet(new_wallet, key)
        with open(wallet_file, "wb") as file:
            file.write(encrypted_wallet)
        print("Wallet address updated.")
        # Restart mining with the new wallet
        miner_process.terminate()
        mine_monero_wallet_saved()  # Restart with new wallet
from cryptography.fernet import Fernet
import json
import base64

# Encryption setup
def generate_key():
    """Generates and saves a key for encryption."""
    return Fernet.generate_key()

def load_key():
    """Loads the existing encryption key."""
    return open("secret.key", "rb").read()

def encrypt_data(data, key):
    """Encrypts the provided data."""
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data, key):
    """Decrypts the provided data."""
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

def encrypt_bytes_to_base64(data):
    """Encrypt bytes and convert to base64 for JSON serialization."""
    return base64.b64encode(data).decode()

def decrypt_base64_to_bytes(base64_data):
    """Convert base64 string back to bytes and decrypt."""
    return base64.b64decode(base64_data.encode())

def mine_monero_advanced_mode():
    """
    Initiates Monero mining in advanced mode by setting up a miner with encrypted wallet address,
    pool URL, and thread count. Saves the configuration in a file 'miningdata' for future use.
    """
    # Load or generate encryption key
    if not os.path.exists("secret.key"):
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    else:
        key = load_key()

    # Check if 'miningdata' file exists and is not empty
    mining_data_file = 'miningdata'
    if os.path.exists(mining_data_file) and os.path.getsize(mining_data_file) > 0:
        with open(mining_data_file, 'rb') as file:
            try:
                mining_data = json.loads(file.read().decode())
                
                # Decrypt saved data
                wallet = decrypt_data(decrypt_base64_to_bytes(mining_data['wallet']), key)
                pool = decrypt_data(decrypt_base64_to_bytes(mining_data['pool']), key)
                threads = int(decrypt_data(decrypt_base64_to_bytes(mining_data['threads']), key))

                # Ask if the user wants to change the saved wallet address
                change_wallet = input(f"Current saved wallet address: {wallet}. Do you want to change it? (yes/no): ").strip().lower()
                if change_wallet == "yes":
                    wallet = input("Enter new Monero wallet address: ")

                # Ask if the user wants to change the saved pool URL
                change_pool = input(f"Current saved pool URL: {pool}. Do you want to change it? (yes/no): ").strip().lower()
                if change_pool == "yes":
                    pool = input("Enter new mining pool URL: ")

                # Ask if the user wants to change the number of threads
                change_threads = input(f"Current saved thread count: {threads}. Do you want to change it? (yes/no): ").strip().lower()
                if change_threads == "yes":
                    threads = int(input("Enter new number of CPU threads to use: "))
                
            except (json.JSONDecodeError, KeyError, TypeError) as e:
                print(f"Error reading mining data: {e}. Starting fresh.")
                wallet = input("Enter your Monero wallet address: ")
                pool = input("Enter your mining pool URL (e.g., pool.supportxmr.com:3333): ")
                threads = int(input("Enter the number of CPU threads to use: "))
    else:
        # If no saved data exists or file is empty, ask for the user's inputs
        wallet = input("Enter your Monero wallet address: ")
        pool = input("Enter your mining pool URL (e.g., pool.supportxmr.com:3333): ")
        threads = int(input("Enter the number of CPU threads to use: "))

    # Encrypt and save the data to 'miningdata'
    encrypted_wallet = encrypt_data(wallet, key)
    encrypted_pool = encrypt_data(pool, key)
    encrypted_threads = encrypt_data(str(threads), key)

    # Convert encrypted data to base64 for JSON compatibility
    mining_data = {
        'wallet': encrypt_bytes_to_base64(encrypted_wallet),
        'pool': encrypt_bytes_to_base64(encrypted_pool),
        'threads': encrypt_bytes_to_base64(encrypted_threads)
    }

    with open(mining_data_file, 'wb') as file:
        file.write(json.dumps(mining_data).encode())
    print(f"Mining data saved securely to {mining_data_file}.")

    # Start mining with the selected or changed wallet, pool, and threads
    miner_process = setup_miner_xmrg(wallet, pool, threads)

    # Monitor mining output
    try:
        monitor_miner_monero(miner_process)
    except Exception as e:
        print(f"An error occurred: {e}")
        miner_process.terminate()
        

def setup_miner_xmrg_cuda(wallet_address, pool_url, threads=4):
    """
    Sets up and starts the Monero mining process using XMRig, dynamically locating the executable.
    
    Args:
        wallet_address (str): Your Monero wallet address.
        pool_url (str): Mining pool URL (e.g., "pool.supportxmr.com:3333").
        threads (int): Number of CPU threads to use.
    
    Returns:
        subprocess.Popen: Process handle for the mining process.
    """
    # Dynamically locate the XMRig executable inside the 'xmrig' folder
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Python script
    xmrig_path = os.path.join(script_dir, "xmrig", "xmrig.exe")# Path to the XMRig executable
    
    # Check if XMRig is installed
    if not os.path.exists(xmrig_path):
        raise FileNotFoundError(f"XMRig not found at {xmrig_path}. Ensure it's in the 'xmrig' folder.")
    
    # Build the XMRig command
    command = [
        xmrig_path,
        "-o", pool_url,
        "-u", wallet_address,
        "-p", "x",  # Default password
        "-t", str(threads),  # Number of CPU threads
        "--donate-level=0",  # Specify the algorithm
        "--keepalive",
        "--cuda" 
        # Optional: Set donation level to 1%
    ]

    # Start the miner
    print("Starting the mining process...")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process
def mine_monero_cuda():
    # User inputs
    """
    Initiates Monero mining by setting up a miner and monitoring its output.

    This function collects user inputs for the Monero wallet address, mining pool URL,
    and the number of CPU threads to use. It then starts the mining process using these
    inputs and monitors the output from the mining process. If an error occurs during
    monitoring, it terminates the miner process.

    Returns:
        None
    """

    wallet = input("Enter your Monero wallet address: ")
    pool = input("Enter your mining pool URL (e.g., pool.supportxmr.com:3333): ")
    threads = int(input("Enter the number of CPU threads to use: "))

    # Start mining
    miner_process = setup_miner_xmrg_cuda(wallet, pool, threads)

    # Monitor mining output
    try:
        monitor_miner_monero(miner_process)
    except Exception as e:
        print(f"An error occurred: {e}")
        miner_process.terminate()
def setup_miner_xmrg_opencl(wallet_address, pool_url, threads=4):
    """
    Sets up and starts the Monero mining process using XMRig, dynamically locating the executable.
    
    Args:
        wallet_address (str): Your Monero wallet address.
        pool_url (str): Mining pool URL (e.g., "pool.supportxmr.com:3333").
        threads (int): Number of CPU threads to use.
    
    Returns:
        subprocess.Popen: Process handle for the mining process.
    """
    # Dynamically locate the XMRig executable inside the 'xmrig' folder
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Python script
    xmrig_path = os.path.join(script_dir, "xmrig", "xmrig.exe")# Path to the XMRig executable
    
    # Check if XMRig is installed
    if not os.path.exists(xmrig_path):
        raise FileNotFoundError(f"XMRig not found at {xmrig_path}. Ensure it's in the 'xmrig' folder.")
    
    # Build the XMRig command
    command = [
        xmrig_path,
        "-o", pool_url,
        "-u", wallet_address,
        "-p", "x",  # Default password
        "-t", str(threads),  # Specify the algorithm
        "--keepalive",# Number of CPU threads
        "--donate-level=0",
        "--opencl" 
        # Optional: Set donation level to 1%
    ]
def mine_monero_opencl():
    # User inputs
    """
    Initiates Monero mining by setting up a miner and monitoring its output.

    This function collects user inputs for the Monero wallet address, mining pool URL,
    and the number of CPU threads to use. It then starts the mining process using these
    inputs and monitors the output from the mining process. If an error occurs during
    monitoring, it terminates the miner process.

    Returns:
        None
    """

    wallet = input("Enter your Monero wallet address: ")
    pool = input("Enter your mining pool URL (e.g., pool.supportxmr.com:3333): ")
    threads = int(input("Enter the number of CPU threads to use: "))

    # Start mining
    miner_process = setup_miner_xmrg_opencl(wallet, pool, threads)

    # Monitor mining output
    try:
        monitor_miner_monero(miner_process)
    except Exception as e:
        print(f"An error occurred: {e}")
        miner_process.terminate()

import os
import subprocess

def xmrig_benchmark(algorithm="rx/0", threads=1):
    """
    Runs XMRig in benchmark mode using the specified executable and captures the output.
    
    Args:
        algorithm (str): The algorithm to benchmark, e.g., "rx/0" for RandomX. Defaults to "rx/0".
        threads (int): Number of CPU threads to use for benchmarking. Defaults to 1.
    
    Returns:
        dict: A dictionary containing benchmark results such as hashrate and details.
    """
    try:
        # Determine the path to the XMRig executable
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Directory of the Python script
        xmrig_path = os.path.join(script_dir, "xmrig", "xmrig.exe")  # Path to the XMRig executable

        # Command to benchmark XMRig
        command = [
            xmrig_path,
            "--bench",
            algorithm,
            "--threads", str(threads)
        ]
        
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"XMRig Benchmark failed: {result.stderr}")
        
        # Process the output
        output = result.stdout
        benchmark_data = {}

        # Example of parsing key information
        for line in output.splitlines():
            if "speed" in line and "H/s" in line:
                speed = line.split()[-2:]  # Extract speed value and unit
                benchmark_data["speed"] = f"{speed[0]} {speed[1]}"
            elif "Threads" in line:
                benchmark_data["threads"] = threads
            elif "Algorithm" in line:
                benchmark_data["algorithm"] = algorithm
        
        return benchmark_data

    except FileNotFoundError:
        print(f"Error: {xmrig_path} not found. Ensure XMRig is installed and the path is correct.")
        return None
    except Exception as e:
        print(f"An error occurred during benchmarking: {e}")
        return None
    


