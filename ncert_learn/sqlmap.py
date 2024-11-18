import subprocess
import logging
import sys
import os
import requests
script_dir = os.path.dirname(os.path.abspath(__file__))
# Add sqlmap folder to Python's system path
sqlmap_path = os.path.join(script_dir, 'sqlmap')  # Path to the SQLmap folder
sys.path.append(sqlmap_path)

# Setup logging to the console
logging.basicConfig(level=logging.INFO)

# SQLmap scan function (basic)
def sqlmap_scan(url, **kwargs):
    """
    Execute the SQLmap scan command with specified parameters.
    """
    command = [sys.executable, 'sqlmap.py', '-u', url, '--batch']
    for key, value in kwargs.items():
        if value is not None:
            command.append(f'--{key}={value}')
    
    try:
        subprocess.run(command,check=True,cwd=sqlmap_path)
        logging.info("SQLmap scan completed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error during SQLmap scan: {e}")




# SQLmap API call function (basic)
def sqlmap_api_call(url, **kwargs):
    """
    Call SQLmap API with specified parameters.
    """
    api_url = f"http://127.0.0.1:8775/scan"
    data = {'url': url}
    data.update(kwargs)
    
    try:
        response = requests.post(api_url, data=data)
        response.raise_for_status()
        logging.info(f"SQLmap API scan started: {response.json()}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during SQLmap API call: {e}")

# --- Simple and Complex SQL Injection Techniques ---
def sqlmap_scan_for_union_based_sql_injection(url):
    """
    Detect UNION-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique="U")

def sqlmap_scan_for_error_based_sql_injection(url):
    """
    Detect error-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique="E")

def sqlmap_scan_for_time_based_sql_injection(url):
    """
    Detect time-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique="T")

def sqlmap_scan_for_boolean_blind_sql_injection(url):
    """
    Detect boolean-based Blind SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique="B")

def sqlmap_scan_for_stacked_queries(url):
    """
    Detect for stacked SQL queries vulnerability.
    """
    sqlmap_scan(url, stacked_queries=True)

def sqlmap_scan_for_tautology_based_sql_injection(url):
    """
    Detect tautology-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique="T")

def sqlmap_scan_for_second_order_sql_injection(url):
    """
    Test for second-order SQL injection vulnerabilities.
    """
    sqlmap_scan(url, second_order=True)

def sqlmap_scan_for_inline_query_sql_injection(url):
    """
    Test for inline query-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, inline_query=True)

def sqlmap_scan_for_blind_time_based_sql_injection(url):
    """
    Test for Blind Time-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique="T", blind=True)

# --- Authentication Handling ---
def sqlmap_scan_with_cookie_based_auth(url, cookie):
    """
    Perform SQLmap scan using cookie-based authentication.
    """
    sqlmap_scan(url, cookie=cookie)

def sqlmap_scan_with_jwt_token(url, jwt_token):
    """
    Perform SQLmap scan using JWT token authentication.
    """
    sqlmap_scan(url, jwt_token=jwt_token)

def sqlmap_scan_with_basic_auth(url, username, password):
    """
    Perform SQLmap scan using HTTP Basic Authentication.
    """
    sqlmap_scan(url, auth_type="Basic", auth_cred=f"{username}:{password}")

def sqlmap_scan_with_digest_auth(url, username, password):
    """
    Perform SQLmap scan using Digest Authentication.
    """
    sqlmap_scan(url, auth_type="Digest", auth_cred=f"{username}:{password}")

def sqlmap_scan_with_ntlm_auth(url, username, password, domain):
    """
    Perform SQLmap scan using NTLM Authentication.
    """
    sqlmap_scan(url, auth_type="NTLM", auth_cred=f"{username}:{password}:{domain}")

# --- Proxy Handling ---
def sqlmap_scan_with_custom_proxy(url, proxy_address):
    """
    Perform scan with custom proxy.
    """
    sqlmap_scan(url, proxy=proxy_address)

def sqlmap_scan_with_socks_proxy(url, socks_proxy):
    """
    Perform scan using SOCKS proxy.
    """
    sqlmap_scan(url, socks_proxy=socks_proxy)

def sqlmap_scan_with_multiple_proxies(url, proxies):
    """
    Perform scan using multiple proxies.
    """
    for proxy in proxies:
        sqlmap_scan_with_custom_proxy(url, proxy)

def sqlmap_scan_with_custom_user_agent(url, user_agent):
    """
    Perform scan with a custom User-Agent header.
    """
    sqlmap_scan(url, user_agent=user_agent)

# --- Request/Response Handling ---
def sqlmap_scan_with_timeout(url, timeout):
    """
    Set a custom timeout for the SQLmap scan.
    """
    sqlmap_scan(url, timeout=timeout)

def sqlmap_scan_with_max_redirects(url, max_redirects):
    """
    Set a maximum number of HTTP redirects for the scan.
    """
    sqlmap_scan(url, max_redirects=max_redirects)

def sqlmap_scan_with_retries(url, retries=3):
    """
    Perform the scan with retry attempts in case of network failures.
    """
    sqlmap_scan(url, retries=retries)

def sqlmap_scan_with_quiet_mode(url):
    """
    Perform scan with minimal output (quiet mode).
    """
    sqlmap_scan(url, quiet=True)

def sqlmap_scan_with_verbosity(url, verbosity_level):
    """
    Set verbosity level for SQLmap scan output.
    """
    sqlmap_scan(url, verbosity=verbosity_level)

# --- OS Command Injection Testing ---
def sqlmap_scan_for_os_command_injection(url):
    """
    Test for OS command injection vulnerabilities.
    """
    sqlmap_scan(url, os_command_injection=True)

def sqlmap_scan_for_os_command_injection_using_shell(url):
    """
    Test for OS command injection using shell methods.
    """
    sqlmap_scan(url, os_command_injection_shell=True)

def sqlmap_scan_for_os_command_injection_with_wildcards(url):
    """
    Test for OS command injection using wildcards.
    """
    sqlmap_scan(url, os_command_injection_wildcards=True)

# --- File Inclusion Testing ---
def sqlmap_scan_for_local_file_inclusion(url, file_path):
    """
    Test for Local File Inclusion (LFI).
    """
    sqlmap_scan(url, lfi=file_path)

def sqlmap_scan_for_remote_file_inclusion(url, file_url):
    """
    Test for Remote File Inclusion (RFI).
    """
    sqlmap_scan(url, rfi=file_url)

def sqlmap_scan_for_file_read(url, file_path):
    """
    Test for reading files from the server via SQL injection.
    """
    sqlmap_scan(url, file_read=file_path)

def sqlmap_scan_for_file_upload(url):
    """
    Test for file upload vulnerabilities.
    """
    sqlmap_scan(url, file_upload=True)

# --- XSS Testing ---
def sqlmap_scan_for_reflected_xss(url):
    """
    Test for reflected XSS vulnerabilities.
    """
    sqlmap_scan(url, reflected_xss=True)

def sqlmap_scan_for_stored_xss(url):
    """
    Test for stored XSS vulnerabilities.
    """
    sqlmap_scan(url, stored_xss=True)

def sqlmap_scan_for_dom_xss(url):
    """
    Test for DOM-based XSS vulnerabilities.
    """
    sqlmap_scan(url, dom_xss=True)

# --- DBMS Enumeration ---
def sqlmap_scan_for_mysql_version(url):
    """
    Enumerate the MySQL version on the target server.
    """
    sqlmap_scan(url, mysql_version=True)

def sqlmap_scan_for_postgresql_version(url):
    """
    Enumerate the PostgreSQL version on the target server.
    """
    sqlmap_scan(url, postgres_version=True)

def sqlmap_scan_for_oracle_version(url):
    """
    Enumerate the Oracle version on the target server.
    """
    sqlmap_scan(url, oracle_version=True)

def sqlmap_scan_for_mssql_version(url):
    """
    Enumerate the MSSQL version on the target server.
    """
    sqlmap_scan(url, mssql_version=True)

# --- SQLmap Error Handling and Logging ---
def sqlmap_scan_with_error_handling(url, retries=3, timeout=30):
    """
    Scan with error handling, retries, and timeout.
    """
    try:
        sqlmap_scan(url, retries=retries, timeout=timeout)
    except Exception as e:
        logging.error(f"Error during SQLmap scan: {e}")
        raise

def sqlmap_scan_with_logging(url, log_file):
    """
    Perform scan with logging to a file.
    """
    logging.basicConfig(filename=log_file, level=logging.INFO)
    sqlmap_scan(url)

def sqlmap_api_status_check():
    """
    Check the status of the SQLmap API.
    """
    api_url = "http://127.0.0.1:8775/status"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            logging.info("SQLmap API is running.")
        else:
            logging.warning("SQLmap API is not responding properly.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error checking SQLmap API status: {e}")

# --- Custom Payload Testing ---
def sqlmap_scan_with_custom_payloads(url, payloads):
    """
    Perform scan with custom SQL injection payloads.
    """
    for payload in payloads:
        sqlmap_scan(url, payload=payload)

# --- Advanced Features ---
def sqlmap_scan_with_network_error_simulation(url):
    """
    Simulate network errors during the scan to test robustness.
    """
    sqlmap_scan(url, network_error_simulation=True)

def sqlmap_scan_with_json_output(url, output_file):
    """
    Perform scan with JSON output.
    """
    sqlmap_scan(url, output_json=True, output_file=output_file)

# --- Bulk Scanning ---
def bulk_sqlmap_scan(urls, **kwargs):
    """
    Perform bulk scanning on multiple URLs.
    """
    for url in urls:
        sqlmap_scan(url, **kwargs)

# --- SQLmap API Management ---
def sqlmap_api_start_scan(url, **kwargs):
    """
    Start a SQLmap scan using the SQLmap API.
    """
    sqlmap_api_call(url, **kwargs)

def sqlmap_api_get_scan_status(scan_id):
    """
    Get the status of an ongoing scan via SQLmap API.
    """
    api_url = f"http://127.0.0.1:8775/scan/{scan_id}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        logging.info(f"Scan status: {response.json()}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching scan status: {e}")

# --- Miscellaneous ---
def sqlmap_scan_with_timeout_and_retries(url, timeout=30, retries=3):
    """
    Perform scan with timeout and retries.
    """
    for _ in range(retries):
        try:
            sqlmap_scan(url, timeout=timeout)
            break
        except Exception as e:
            logging.warning(f"Retrying scan due to error: {e}")

# --- SQLmap API Termination ---
def sqlmap_api_terminate_scan(scan_id):
    """
    Terminate an ongoing scan via SQLmap API.
    """
    api_url = f"http://127.0.0.1:8775/scan/{scan_id}/kill"
    try:
        response = requests.post(api_url)
        response.raise_for_status()
        logging.info(f"Scan {scan_id} terminated successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error terminating scan: {e}")


# Advanced SQLi Detection
def sqlmap_scan_for_union_based_sql_injection(url):
    """
    Detect UNION-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, union_based=True)

def sqlmap_scan_for_syntax_based_sql_injection(url):
    """
    Detect syntax-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, syntax_based=True)

def sqlmap_scan_for_time_based_sql_injection(url):
    """
    Detect time-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, time_based=True)

def sqlmap_scan_for_error_based_sql_injection(url):
    """
    Detect error-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, error_based=True)

def sqlmap_scan_for_blind_sql_injection(url):
    """
    Detect Blind SQL injection vulnerabilities.
    """
    sqlmap_scan(url, blind=True)

# Advanced Response Handling
def sqlmap_scan_with_response_timeout(url, timeout):
    """
    Scan with custom response timeout.
    """
    sqlmap_scan(url, timeout=timeout)

def sqlmap_scan_with_retry(url, retries=3):
    """
    Scan with retries in case of network failures.
    """
    sqlmap_scan(url, retries=retries)

def sqlmap_scan_with_max_redirects(url, max_redirects):
    """
    Limit the number of HTTP redirects during the scan.
    """
    sqlmap_scan(url, max_redirects=max_redirects)

# Advanced Authentication
def sqlmap_scan_with_basic_auth(url, username, password):
    """
    Perform a scan using HTTP Basic Authentication.
    """
    sqlmap_scan(url, auth_type='Basic', auth_cred=f"{username}:{password}")

def sqlmap_scan_with_digest_auth(url, username, password):
    """
    Perform a scan using Digest Authentication.
    """
    sqlmap_scan(url, auth_type='Digest', auth_cred=f"{username}:{password}")

def sqlmap_scan_with_ntlm_auth(url, username, password, domain):
    """
    Perform a scan using NTLM Authentication.
    """
    sqlmap_scan(url, auth_type='NTLM', auth_cred=f"{username}:{password}:{domain}")

# Payload Handling
def sqlmap_scan_with_custom_payload(url, payload_file):
    """
    Use a custom payload list from a file.
    """
    sqlmap_scan(url, payload_file=payload_file)

def sqlmap_scan_with_multiple_payloads(url, payload_files):
    """
    Use multiple payload files for a more exhaustive scan.
    """
    for payload_file in payload_files:
        sqlmap_scan_with_custom_payload(url, payload_file)

# Proxy and Network Configuration
def sqlmap_scan_with_custom_proxy(url, proxy_address):
    """
    Use a custom proxy for the scan.
    """
    sqlmap_scan(url, proxy=proxy_address)

def sqlmap_scan_with_socks_proxy(url, socks_proxy):
    """
    Use SOCKS proxy for the scan.
    """
    sqlmap_scan(url, socks_proxy=socks_proxy)

def sqlmap_scan_with_multiple_proxies(url, proxies):
    """
    Use multiple proxies for anonymity during the scan.
    """
    for proxy in proxies:
        sqlmap_scan_with_custom_proxy(url, proxy)

# Response Handling and Logging
def sqlmap_scan_with_quiet_mode(url):
    """
    Perform the scan with minimal output (quiet mode).
    """
    sqlmap_scan(url, quiet=True)

def sqlmap_scan_with_verbosity(url, verbosity_level):
    """
    Increase the verbosity of the scan output.
    """
    sqlmap_scan(url, verbosity=verbosity_level)

def sqlmap_scan_with_output_log(url, output_file):
    """
    Save scan output to a log file.
    """
    sqlmap_scan(url, output=output_file)

# Scan Type Specific Functions
def sqlmap_scan_with_sqli_check(url):
    """
    Perform a SQL injection check on the URL.
    """
    sqlmap_scan(url, sqli=True)

def sqlmap_scan_with_xss_check(url):
    """
    Perform an XSS check on the URL.
    """
    sqlmap_scan(url, xss=True)

def sqlmap_scan_for_file_inclusion(url, file_path):
    """
    Test for Local File Inclusion (LFI) vulnerabilities.
    """
    sqlmap_scan(url, lfi=file_path)

def sqlmap_scan_for_remote_file_inclusion(url, file_url):
    """
    Test for Remote File Inclusion (RFI) vulnerabilities.
    """
    sqlmap_scan(url, rfi=file_url)

# Advanced Injection Handling
def sqlmap_scan_with_stacked_queries(url):
    """
    Test for stacked SQL query vulnerabilities.
    """
    sqlmap_scan(url, stacked_queries=True)

def sqlmap_scan_with_sqli_privesc(url):
    """
    Test for SQL injection privilege escalation.
    """
    sqlmap_scan(url, sqli_privesc=True)

def sqlmap_scan_for_boolean_blind(url):
    """
    Test for Boolean Blind SQL injection vulnerabilities.
    """
    sqlmap_scan(url, boolean_blind=True)

def sqlmap_scan_for_time_based_blind(url):
    """
    Test for Time-Based Blind SQL injection vulnerabilities.
    """
    sqlmap_scan(url, time_based_blind=True)

def sqlmap_scan_with_union_query_injection(url):
    """
    Perform UNION-based query injection.
    """
    sqlmap_scan(url, union=True)

# File and Directory Traversal
def sqlmap_scan_for_directory_traversal(url):
    """
    Scan for directory traversal vulnerabilities.
    """
    sqlmap_scan(url, dir_traversal=True)

def sqlmap_scan_for_file_read(url, file_path):
    """
    Read files from the server using SQL injection.
    """
    sqlmap_scan(url, file_read=file_path)

def sqlmap_scan_for_file_upload(url):
    """
    Test for file upload vulnerabilities.
    """
    sqlmap_scan(url, file_upload=True)

# Custom Headers and Cookies
def sqlmap_scan_with_custom_headers(url, headers):
    """
    Perform scan with custom HTTP headers.
    """
    sqlmap_scan(url, headers=headers)

def sqlmap_scan_with_custom_cookies(url, cookies):
    """
    Perform scan with custom cookies.
    """
    sqlmap_scan(url, cookies=cookies)

def sqlmap_scan_with_user_agent(url, user_agent):
    """
    Set custom User-Agent for the scan.
    """
    sqlmap_scan(url, user_agent=user_agent)

# DBMS Enumeration
def sqlmap_scan_for_mysql_version(url):
    """
    Enumerate the MySQL version on the target server.
    """
    sqlmap_scan(url, mysql_version=True)

def sqlmap_scan_for_postgresql_version(url):
    """
    Enumerate the PostgreSQL version on the target server.
    """
    sqlmap_scan(url, postgres_version=True)

def sqlmap_scan_for_oracle_version(url):
    """
    Enumerate the Oracle version on the target server.
    """
    sqlmap_scan(url, oracle_version=True)

def sqlmap_scan_for_mssql_version(url):
    """
    Enumerate the MSSQL version on the target server.
    """
    sqlmap_scan(url, mssql_version=True)

# Cross-Site Scripting (XSS) Testing
def sqlmap_scan_for_reflected_xss(url):
    """
    Test for Reflected XSS vulnerabilities.
    """
    sqlmap_scan(url, reflected_xss=True)

def sqlmap_scan_for_stored_xss(url):
    """
    Test for Stored XSS vulnerabilities.
    """
    sqlmap_scan(url, stored_xss=True)

def sqlmap_scan_for_dom_xss(url):
    """
    Test for DOM-based XSS vulnerabilities.
    """
    sqlmap_scan(url, dom_xss=True)

# Session Management and Authentication
def sqlmap_scan_with_session_storage(url, session_data):
    """
    Test SQL injection with session storage data.
    """
    sqlmap_scan(url, session_storage=session_data)

def sqlmap_scan_with_cookie_based_auth(url, cookie):
    """
    Test SQL injection with cookie-based authentication.
    """
    sqlmap_scan(url, cookie=cookie)

def sqlmap_scan_with_basic_auth(url, username, password):
    """
    Test SQL injection with basic HTTP authentication.
    """
    sqlmap_scan(url, auth_type="Basic", auth_cred=f"{username}:{password}")

def sqlmap_scan_with_jwt_auth(url, jwt_token):
    """
    Test SQL injection with JWT-based authentication.
    """
    sqlmap_scan(url, jwt_token=jwt_token)

# SQLmap Cleanup
def sqlmap_cleanup():
    """
    Clean up after the SQLmap scan.
    """
    logging.info("Cleaning up resources after scan.")
    # Add your cleanup code here (e.g., removing temporary files or logs)



# --- Advanced SQL Injection Detection ---

def sqlmap_scan_for_union_based_sql_injection(url):
    """
    Detect UNION-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, union_based=True)

def sqlmap_scan_for_error_based_sql_injection(url):
    """
    Detect error-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, error_based=True)

def sqlmap_scan_for_time_based_sql_injection(url):
    """
    Detect time-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, time_based=True)

def sqlmap_scan_for_boolean_blind_sql_injection(url):
    """
    Detect boolean-based Blind SQL injection vulnerabilities.
    """
    sqlmap_scan(url, boolean_blind=True)

def sqlmap_scan_for_stack_based_sql_injection(url):
    """
    Detect stack-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, stack_based=True)

def sqlmap_scan_for_tautology_based_sql_injection(url):
    """
    Detect tautology-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, tautology_based=True)

# --- Session Handling Functions ---

def sqlmap_scan_with_cookie_based_auth(url, cookie):
    """
    Perform SQLmap scan using cookie-based authentication.
    """
    sqlmap_scan(url, cookie=cookie)

def sqlmap_scan_with_jwt_token(url, jwt_token):
    """
    Perform SQLmap scan using JWT token authentication.
    """
    sqlmap_scan(url, jwt_token=jwt_token)

def sqlmap_scan_with_basic_auth(url, username, password):
    """
    Perform SQLmap scan using HTTP Basic Authentication.
    """
    sqlmap_scan(url, auth_type="Basic", auth_cred=f"{username}:{password}")

def sqlmap_scan_with_digest_auth(url, username, password):
    """
    Perform SQLmap scan using Digest Authentication.
    """
    sqlmap_scan(url, auth_type="Digest", auth_cred=f"{username}:{password}")

def sqlmap_scan_with_ntlm_auth(url, username, password, domain):
    """
    Perform SQLmap scan using NTLM Authentication.
    """
    sqlmap_scan(url, auth_type="NTLM", auth_cred=f"{username}:{password}:{domain}")

# --- Proxy and Network Configuration ---

def sqlmap_scan_with_custom_proxy(url, proxy_address):
    """
    Perform scan with custom proxy.
    """
    sqlmap_scan(url, proxy=proxy_address)

def sqlmap_scan_with_socks_proxy(url, socks_proxy):
    """
    Perform scan using SOCKS proxy.
    """
    sqlmap_scan(url, socks_proxy=socks_proxy)

def sqlmap_scan_with_multiple_proxies(url, proxies):
    """
    Perform scan using multiple proxies.
    """
    for proxy in proxies:
        sqlmap_scan_with_custom_proxy(url, proxy)

def sqlmap_scan_with_custom_user_agent(url, user_agent):
    """
    Perform scan with a custom User-Agent header.
    """
    sqlmap_scan(url, user_agent=user_agent)

# --- Advanced Request and Response Handling ---

def sqlmap_scan_with_timeout(url, timeout):
    """
    Set a custom timeout for the SQLmap scan.
    """
    sqlmap_scan(url, timeout=timeout)

def sqlmap_scan_with_max_redirects(url, max_redirects):
    """
    Set a maximum number of HTTP redirects for the scan.
    """
    sqlmap_scan(url, max_redirects=max_redirects)

def sqlmap_scan_with_retries(url, retries=3):
    """
    Perform the scan with retry attempts in case of network failures.
    """
    sqlmap_scan(url, retries=retries)

def sqlmap_scan_with_quiet_mode(url):
    """
    Perform scan with minimal output (quiet mode).
    """
    sqlmap_scan(url, quiet=True)

def sqlmap_scan_with_verbosity(url, verbosity_level):
    """
    Set verbosity level for SQLmap scan output.
    """
    sqlmap_scan(url, verbosity=verbosity_level)

# --- Blind SQL Injection Testing ---

def sqlmap_scan_for_boolean_based_blind_injection(url):
    """
    Test for Boolean Blind SQL injection.
    """
    sqlmap_scan(url, boolean_blind=True)

def sqlmap_scan_for_time_based_blind_injection(url):
    """
    Test for Time-Based Blind SQL injection.
    """
    sqlmap_scan(url, time_based_blind=True)

def sqlmap_scan_for_stack_based_blind_injection(url):
    """
    Test for Stack-Based Blind SQL injection.
    """
    sqlmap_scan(url, stack_based_blind=True)

# --- OS Command Injection Testing ---

def sqlmap_scan_for_os_command_injection(url):
    """
    Test for OS command injection vulnerabilities.
    """
    sqlmap_scan(url, os_command_injection=True)

def sqlmap_scan_for_os_command_injection_using_shell(url):
    """
    Test for OS command injection using shell methods.
    """
    sqlmap_scan(url, os_command_injection_shell=True)

def sqlmap_scan_for_os_command_injection_with_wildcards(url):
    """
    Test for OS command injection using wildcards.
    """
    sqlmap_scan(url, os_command_injection_wildcards=True)

# --- File Inclusion Testing ---

def sqlmap_scan_for_local_file_inclusion(url, file_path):
    """
    Test for Local File Inclusion (LFI).
    """
    sqlmap_scan(url, lfi=file_path)

def sqlmap_scan_for_remote_file_inclusion(url, file_url):
    """
    Test for Remote File Inclusion (RFI).
    """
    sqlmap_scan(url, rfi=file_url)

def sqlmap_scan_for_file_read(url, file_path):
    """
    Test for reading files from the server via SQL injection.
    """
    sqlmap_scan(url, file_read=file_path)

def sqlmap_scan_for_file_upload(url):
    """
    Test for file upload vulnerabilities.
    """
    sqlmap_scan(url, file_upload=True)

# --- SQLmap Cleanup Function ---

def sqlmap_cleanup():
    """
    Clean up after the SQLmap scan.
    """
    logging.info("Cleaning up resources after scan.")
    # Add your cleanup code here (e.g., removing temporary files or logs)

# --- Custom Payload Handling ---

def sqlmap_scan_with_custom_payload(url, payload_file):
    """
    Test with custom payloads from a file.
    """
    sqlmap_scan(url, payload_file=payload_file)

def sqlmap_scan_with_multiple_payloads(url, payload_files):
    """
    Test with multiple custom payloads from different files.
    """
    for payload_file in payload_files:
        sqlmap_scan_with_custom_payload(url, payload_file)

def sqlmap_scan_with_random_payloads(url):
    """
    Test using randomly generated payloads.
    """
    sqlmap_scan(url, random_payloads=True)

# --- Cross-Site Scripting (XSS) Testing ---

def sqlmap_scan_for_reflected_xss(url):
    """
    Test for reflected XSS vulnerabilities.
    """
    sqlmap_scan(url, reflected_xss=True)

def sqlmap_scan_for_stored_xss(url):
    """
    Test for stored XSS vulnerabilities.
    """
    sqlmap_scan(url, stored_xss=True)

def sqlmap_scan_for_dom_xss(url):
    """
    Test for DOM-based XSS vulnerabilities.
    """
    sqlmap_scan(url, dom_xss=True)

# --- SQLmap Database Management System (DBMS) Enumeration ---

def sqlmap_scan_for_mysql_version(url):
    """
    Enumerate the MySQL version on the target server.
    """
    sqlmap_scan(url, mysql_version=True)

def sqlmap_scan_for_postgresql_version(url):
    """
    Enumerate the PostgreSQL version on the target server.
    """
    sqlmap_scan(url, postgres_version=True)

def sqlmap_scan_for_oracle_version(url):
    """
    Enumerate the Oracle version on the target server.
    """
    sqlmap_scan(url, oracle_version=True)

def sqlmap_scan_for_mssql_version(url):
    """
    Enumerate the MSSQL version on the target server.
    """
    sqlmap_scan(url, mssql_version=True)

# --- SQLmap Error Handling and Logging ---

def sqlmap_scan_with_error_handling(url, retries=3, timeout=30):
    """
    Scan with error handling, retries, and timeout.
    """
    try:
        sqlmap_scan(url, retries=retries, timeout=timeout)
    except Exception as e:
        logging.error(f"Error during SQLmap scan: {e}")
        raise



# --- Enhanced SQL Injection Detection ---
def sqlmap_scan_for_union_based_sql_injection(url):
    """
    Detect UNION-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique='U')

def sqlmap_scan_for_error_based_sql_injection(url):
    """
    Detect error-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique='E')

def sqlmap_scan_for_time_based_sql_injection(url):
    """
    Detect time-based SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique='T')

def sqlmap_scan_for_boolean_blind_sql_injection(url):
    """
    Detect boolean-based Blind SQL injection vulnerabilities.
    """
    sqlmap_scan(url, technique='B')

def sqlmap_scan_for_stacked_queries(url):
    """
    Detect for stacked SQL queries vulnerability.
    """
    sqlmap_scan(url, stacked_queries=True)

def sqlmap_scan_for_second_order_sql_injection(url):
    """
    Test for second-order SQL injection vulnerabilities.
    """
    sqlmap_scan(url, second_order=True)

# --- Session Handling Functions ---
def sqlmap_scan_with_cookie_based_auth(url, cookie):
    """
    Perform SQLmap scan using cookie-based authentication.
    """
    sqlmap_scan(url, cookie=cookie)

def sqlmap_scan_with_jwt_token(url, jwt_token):
    """
    Perform SQLmap scan using JWT token authentication.
    """
    sqlmap_scan(url, jwt_token=jwt_token)

def sqlmap_scan_with_basic_auth(url, username, password):
    """
    Perform SQLmap scan using HTTP Basic Authentication.
    """
    sqlmap_scan(url, auth_type="Basic", auth_cred=f"{username}:{password}")

def sqlmap_scan_with_digest_auth(url, username, password):
    """
    Perform SQLmap scan using Digest Authentication.
    """
    sqlmap_scan(url, auth_type="Digest", auth_cred=f"{username}:{password}")

def sqlmap_scan_with_ntlm_auth(url, username, password, domain):
    """
    Perform SQLmap scan using NTLM Authentication.
    """
    sqlmap_scan(url, auth_type="NTLM", auth_cred=f"{username}:{password}:{domain}")

# --- Proxy and Network Configuration ---
def sqlmap_scan_with_custom_proxy(url, proxy_address):
    """
    Perform scan with custom proxy.
    """
    sqlmap_scan(url, proxy=proxy_address)

def sqlmap_scan_with_socks_proxy(url, socks_proxy):
    """
    Perform scan using SOCKS proxy.
    """
    sqlmap_scan(url, socks_proxy=socks_proxy)

def sqlmap_scan_with_multiple_proxies(url, proxies):
    """
    Perform scan using multiple proxies.
    """
    for proxy in proxies:
        sqlmap_scan_with_custom_proxy(url, proxy)

def sqlmap_scan_with_custom_user_agent(url, user_agent):
    """
    Perform scan with a custom User-Agent header.
    """
    sqlmap_scan(url, user_agent=user_agent)

# --- Advanced Request and Response Handling ---
def sqlmap_scan_with_timeout(url, timeout):
    """
    Set a custom timeout for the SQLmap scan.
    """
    sqlmap_scan(url, timeout=timeout)

def sqlmap_scan_with_max_redirects(url, max_redirects):
    """
    Set a maximum number of HTTP redirects for the scan.
    """
    sqlmap_scan(url, max_redirects=max_redirects)

def sqlmap_scan_with_retries(url, retries=3):
    """
    Perform the scan with retry attempts in case of network failures.
    """
    sqlmap_scan(url, retries=retries)

def sqlmap_scan_with_quiet_mode(url):
    """
    Perform scan with minimal output (quiet mode).
    """
    sqlmap_scan(url, quiet=True)

def sqlmap_scan_with_verbosity(url, verbosity_level):
    """
    Set verbosity level for SQLmap scan output.
    """
    sqlmap_scan(url, verbosity=verbosity_level)

# --- OS Command Injection Testing ---
def sqlmap_scan_for_os_command_injection(url):
    """
    Test for OS command injection vulnerabilities.
    """
    sqlmap_scan(url, os_command_injection=True)

def sqlmap_scan_for_os_command_injection_using_shell(url):
    """
    Test for OS command injection using shell methods.
    """
    sqlmap_scan(url, os_command_injection_shell=True)

def sqlmap_scan_for_os_command_injection_with_wildcards(url):
    """
    Test for OS command injection using wildcards.
    """
    sqlmap_scan(url, os_command_injection_wildcards=True)

# --- File Inclusion Testing ---
def sqlmap_scan_for_local_file_inclusion(url, file_path):
    """
    Test for Local File Inclusion (LFI).
    """
    sqlmap_scan(url, lfi=file_path)

def sqlmap_scan_for_remote_file_inclusion(url, file_url):
    """
    Test for Remote File Inclusion (RFI).
    """
    sqlmap_scan(url, rfi=file_url)

def sqlmap_scan_for_file_read(url, file_path):
    """
    Test for reading files from the server via SQL injection.
    """
    sqlmap_scan(url, file_read=file_path)

def sqlmap_scan_for_file_upload(url):
    """
    Test for file upload vulnerabilities.
    """
    sqlmap_scan(url, file_upload=True)

# --- SQLmap Cleanup Function ---
def sqlmap_cleanup():
    """
    Clean up after the SQLmap scan.
    """
    logging.info("Cleaning up resources after scan.")
    # Add your cleanup code here (e.g., removing temporary files or logs)

# --- Custom Payload Handling ---
def sqlmap_scan_with_custom_payload(url, payload_file):
    """
    Test with custom payloads from a file.
    """
    sqlmap_scan(url, payload_file=payload_file)

def sqlmap_scan_with_multiple_payloads(url, payload_files):
    """
    Test with multiple custom payloads from different files.
    """
    for payload_file in payload_files:
        sqlmap_scan_with_custom_payload(url, payload_file)

def sqlmap_scan_with_random_payloads(url):
    """
    Test using randomly generated payloads.
    """
    sqlmap_scan(url, random_payloads=True)

# --- Cross-Site Scripting (XSS) Testing ---
def sqlmap_scan_for_reflected_xss(url):
    """
    Test for reflected XSS vulnerabilities.
    """
    sqlmap_scan(url, reflected_xss=True)

def sqlmap_scan_for_stored_xss(url):
    """
    Test for stored XSS vulnerabilities.
    """
    sqlmap_scan(url, stored_xss=True)

def sqlmap_scan_for_dom_xss(url):
    """
    Test for DOM-based XSS vulnerabilities.
    """
    sqlmap_scan(url, dom_xss=True)

# --- SQLmap Database Management System (DBMS) Enumeration ---
def sqlmap_scan_for_mysql_version(url):
    """
    Enumerate the MySQL version on the target server.
    """
    sqlmap_scan(url, mysql_version=True)

def sqlmap_scan_for_postgresql_version(url):
    """
    Enumerate the PostgreSQL version on the target server.
    """
    sqlmap_scan(url, postgres_version=True)

def sqlmap_scan_for_oracle_version(url):
    """
    Enumerate the Oracle version on the target server.
    """
    sqlmap_scan(url, oracle_version=True)

def sqlmap_scan_for_mssql_version(url):
    """
    Enumerate the MSSQL version on the target server.
    """
    sqlmap_scan(url, mssql_version=True)

# --- SQLmap Error Handling and Logging ---
def sqlmap_scan_with_error_handling(url, retries=3, timeout=30):
    """
    Scan with error handling, retries, and timeout.
    """
    try:
        sqlmap_scan(url, retries=retries, timeout=timeout)
    except Exception as e:
        logging.error(f"Error during SQLmap scan: {e}")
        raise

