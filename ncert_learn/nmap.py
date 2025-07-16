import nmap
import sys
import logging

# Set up logging configuration to display messages in the console
logging.basicConfig(level=logging.INFO, format='%(message)s')

def nmap_scan(target, arguments):
    """
    Executes a basic Nmap scan on the target with the specified arguments.
    
    Args:
        target (str): The IP address or hostname to scan.
        arguments (str): The Nmap command line arguments for the scan.
    """
    try:
        nm = nmap.PortScanner()
        logging.info(f"Starting Scan on {target} with arguments: {arguments}")
        nm.scan(hosts=target, arguments=arguments)
        for host in nm.all_hosts():
            logging.info(f"Host: {host} ({nm[host].hostname()})")
            logging.info(f"State: {nm[host].state()}")
            for protocol in nm[host].all_protocols():
                logging.info(f"Protocol: {protocol}")
                lport = nm[host][protocol].keys()
                for port in lport:
                    logging.info(f"Port: {port}\tState: {nm[host][protocol][port]['state']}")
        logging.info(f"Scan completed for {target} with arguments: {arguments}")
    except nmap.nmap.PortScannerError as e:
        logging.error(f"PortScannerError: {e}")
    except Exception as e:
        logging.error(f"Error during scan: {e}")
        sys.exit(1)

def nmap_intense_scan(target):
    """
    Performs an intense scan on the target using the '-T4 -A -v' options for detailed service detection, OS detection, and version scanning.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-T4 -A -v')

def nmap_quick_scan(target):
    """
    Performs a quick scan on the target using the '-T4 -F' options for a fast scan.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-T4 -F')

def nmap_ping_sweep(target_range):
    """
    Performs a ping sweep to identify live hosts within a range of IP addresses using the '-sn' option.
    
    Args:
        target_range (str): The IP range to scan (e.g., '192.168.1.0/24').
    """
    nmap_scan(target_range, '-sn')

def nmap_os_detection(target):
    """
    Detects the operating system of the target host using the '-O' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-O')

def nmap_service_version_detection(target):
    """
    Detects the version of services running on the target host using the '-sV' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sV')

def nmap_tcp_connect_scan(target):
    """
    Performs a TCP connect scan on the target using the '-sT' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sT')

def nmap_syn_scan(target):
    """
    Performs a SYN scan on the target using the '-sS' option (stealth scan).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sS')

def nmap_udp_scan(target):
    """
    Performs a UDP scan on the target using the '-sU' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sU')

def nmap_traceroute_scan(target):
    """
    Performs a traceroute scan on the target using the '--traceroute' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--traceroute')

def nmap_vulnerability_scan(target):
    """
    Performs a vulnerability scan on the target using the '--script=vuln' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=vuln')

def nmap_stealth_scan(target):
    """
    Performs a stealth scan on the target using the '-sS' option (half-open scan).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sS')

def nmap_ack_scan(target):
    """
    Performs an ACK scan on the target using the '-sA' option (for firewall/packet filtering).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sA')

def nmap_window_scan(target):
    """
    Performs a Window scan on the target using the '-sW' option (used for OS fingerprinting).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sW')

def nmap_masquerade_scan(target):
    """
    Performs a Masquerade scan on the target using the '-sM' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sM')

def nmap_decoy_scan(target):
    """
    Performs a Decoy scan on the target using the '-D RND:10' option (using random decoys).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-D RND:10')

def nmap_fin_scan(target):
    """
    Performs a FIN scan on the target using the '-sF' option (attempts to bypass firewalls).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sF')

def nmap_xmas_scan(target):
    """
    Performs an Xmas scan on the target using the '-sX' option (sets odd flags).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sX')

def nmap_null_scan(target):
    """
    Performs a Null scan on the target using the '-sN' option (no flags set).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sN')

def nmap_ping_scan(target):
    """
    Performs a ping scan on the target using the '-sn' option (host discovery only).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-sn')

def nmap_sweep_scan(target_range):
    """
    Performs a sweep scan to check multiple ports across a range of hosts.
    
    Args:
        target_range (str): The IP range to scan (e.g., '192.168.1.0/24').
    """
    nmap_scan(target_range, '-PS22')

def nmap_ftp_scan(target):
    """
    Performs an FTP scan on the target using the '--script=ftp-anon' option (checks for anonymous access).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-p 21 --script=ftp-anon')

def nmap_smtp_scan(target):
    """
    Performs an SMTP scan on the target using the '--script=smtp-open-relay' option (checks for open relay).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-p 25 --script=smtp-open-relay')

def nmap_dns_scan(target):
    """
    Performs a DNS scan on the target using the '--script=dns-brute' option (brute-forces DNS names).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-p 53 --script=dns-brute')

def nmap_http_scan(target):
    """
    Performs an HTTP scan on the target using the '--script=http-headers' option (fetches HTTP headers).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-p 80 --script=http-headers')

def nmap_pop3_scan(target):
    """
    Performs a POP3 scan on the target using the '--script=pop3-capabilities' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-p 110 --script=pop3-capabilities')

def nmap_ssh_scan(target):
    """
    Performs an SSH scan on the target using the '--script=ssh-brute' option (for brute-forcing SSH credentials).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-p 22 --script=ssh-brute')

def nmap_mysql_scan(target):
    """
    Performs a MySQL scan on the target using the '--script=mysql-info' option (fetches MySQL information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-p 3306 --script=mysql-info')

def nmap_smb_vuln_scan(target):
    """
    Performs an SMB vulnerability scan on the target using the '--script=smb-vuln*' option (checks for SMB vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-vuln*')

def nmap_http_favicon_scan(target):
    """
    Performs an HTTP favicon scan on the target using the '--script=http-favicon' option (grabs the favicon from the HTTP server).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-favicon')

def nmap_smb_share_scan(target):
    """
    Performs an SMB share scan on the target using the '--script=smb-enum-shares' option (enumerates SMB shares).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-enum-shares')

def nmap_traffic_analysis(target):
    """
    Performs traffic analysis on the target using the '--script=traffic-analysis' option (detects network traffic anomalies).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=traffic-analysis')

def nmap_smtp_vuln_scan(target):
    """
    Performs an SMTP vulnerability scan on the target using the '--script=smtp-vuln*' option (checks for vulnerabilities in SMTP).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-vuln*')

def nmap_rdp_vuln_scan(target):
    """
    Performs a Remote Desktop Protocol (RDP) vulnerability scan on the target using the '--script=rdp-vuln-ms12-020' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=rdp-vuln-ms12-020')

def nmap_irc_scan(target):
    """
    Performs an IRC scan on the target using the '--script=irc-info' option (retrieves information about IRC services).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=irc-info')

def nmap_ldap_scan(target):
    """
    Performs an LDAP scan on the target using the '--script=ldap-search' option (performs LDAP directory search).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ldap-search')

def nmap_snmp_scan(target):
    """
    Performs an SNMP scan on the target using the '--script=snmp-brute' option (brute forces SNMP community strings).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=snmp-brute')

def nmap_dns_vuln_scan(target):
    """
    Performs a DNS vulnerability scan on the target using the '--script=dns-vuln*' option (checks for DNS-related vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dns-vuln*')

def nmap_http_auth_scan(target):
    """
    Performs an HTTP authentication scan on the target using the '--script=http-auth' option (tests for authentication methods).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-auth')

def nmap_telnet_scan(target):
    """
    Performs a Telnet scan on the target using the '--script=telnet-brute' option (brute forces Telnet login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=telnet-brute')

def nmap_mysql_brute_scan(target):
    """
    Performs a MySQL brute-force scan on the target using the '--script=mysql-brute' option (brute forces MySQL login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mysql-brute')

def nmap_smb_info_scan(target):
    """
    Performs an SMB information scan on the target using the '--script=smb-os-fingerprint' option (retrieves SMB OS information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-os-fingerprint')

def nmap_nfs_scan(target):
    """
    Performs an NFS scan on the target using the '--script=nfs-showmount' option (retrieves NFS share information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=nfs-showmount')

def nmap_mongodb_scan(target):
    """
    Performs a MongoDB scan on the target using the '--script=mongodb-database' option (retrieves MongoDB database information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mongodb-database')

def nmap_dhcp_scan(target):
    """
    Performs a DHCP scan on the target using the '--script=dhcp-discover' option (discovers DHCP servers).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dhcp-discover')

def nmap_vnc_scan(target):
    """
    Performs a VNC scan on the target using the '--script=vnc-info' option (retrieves VNC information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=vnc-info')

def nmap_ftp_anonymous_scan(target):
    """
    Performs an FTP anonymous scan on the target using the '--script=ftp-anon' option (checks for anonymous FTP login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-anon')

def nmap_smtp_enum_scan(target):
    """
    Performs an SMTP enumeration scan on the target using the '--script=smtp-commands' option (enumerates SMTP commands).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-commands')

def nmap_ftp_banners_scan(target):
    """
    Performs an FTP banner scan on the target using the '--script=ftp-banner' option (retrieves FTP service banners).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-banner')

def nmap_smb_enum_users_scan(target):
    """
    Performs an SMB user enumeration scan on the target using the '--script=smb-enum-users' option (enumerates SMB users).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-enum-users')

def nmap_ssh_enum_users_scan(target):
    """
    Performs an SSH user enumeration scan on the target using the '--script=ssh-brute' option (brute forces SSH users).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssh-brute')

def nmap_pop3_brute_scan(target):
    """
    Performs a POP3 brute-force scan on the target using the '--script=pop3-brute' option (brute forces POP3 credentials).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=pop3-brute')

def nmap_tcp_ping_scan(target):
    """
    Performs a TCP ping scan on the target using the '-PS' option (attempts to ping a target using TCP).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '-PS')

def nmap_ssl_scan(target):
    """
    Performs an SSL scan on the target using the '--script=ssl-cert' option (retrieves SSL certificate information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssl-cert')

def nmap_ssl_vuln_scan(target):
    """
    Performs an SSL vulnerability scan on the target using the '--script=ssl-enum-ciphers' option (checks SSL ciphers for weaknesses).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssl-enum-ciphers')

def nmap_smb_file_scan(target):
    """
    Performs an SMB file scan on the target using the '--script=smb-ls' option (lists files on an SMB share).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-ls')

def nmap_ftp_banners_scan(target):
    """
    Performs a banner grabbing scan for FTP services using the '--script=ftp-banners' option.
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-banners')

def nmap_vuln_detection_scan(target):
    """
    Performs a generic vulnerability detection scan on the target using the '--script=vuln' option (checks for known vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=vuln')
def nmap_smtp_open_scan(target):
    """
    Performs an SMTP open scan on the target using the '--script=smtp-open' option (checks for open SMTP servers).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-open')

def nmap_http_methods_scan(target):
    """
    Performs an HTTP methods scan on the target using the '--script=http-methods' option (checks allowed HTTP methods).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-methods')

def nmap_ssh_vuln_scan(target):
    """
    Performs an SSH vulnerability scan on the target using the '--script=ssh-vuln*' option (checks for SSH vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssh-vuln*')

def nmap_http_xss_scan(target):
    """
    Performs an HTTP Cross-site Scripting (XSS) scan on the target using the '--script=http-xss' option (checks for XSS vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-xss')

def nmap_ftp_anonymous_scan(target):
    """
    Performs an FTP anonymous login scan on the target using the '--script=ftp-anon' option (checks for FTP anonymous access).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-anon')

def nmap_dhcp_discovery_scan(target):
    """
    Performs a DHCP discovery scan on the target using the '--script=dhcp-discover' option (discovers DHCP servers).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dhcp-discover')

def nmap_nfs_mount_scan(target):
    """
    Performs an NFS mount scan on the target using the '--script=nfs-mount' option (retrieves NFS mount points).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=nfs-mount')

def nmap_smtp_brute_scan(target):
    """
    Performs an SMTP brute-force scan on the target using the '--script=smtp-brute' option (attempts to brute-force SMTP logins).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-brute')

def nmap_smb_brute_scan(target):
    """
    Performs an SMB brute-force scan on the target using the '--script=smb-brute' option (attempts to brute-force SMB logins).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-brute')

def nmap_ldap_enum_scan(target):
    """
    Performs an LDAP enumeration scan on the target using the '--script=ldap-brute' option (brute forces LDAP credentials).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ldap-brute')

def nmap_http_sitemap_scan(target):
    """
    Performs an HTTP sitemap scan on the target using the '--script=http-sitemap' option (grabs HTTP sitemap information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-sitemap')

def nmap_ftp_version_scan(target):
    """
    Performs an FTP version scan on the target using the '--script=ftp-versions' option (retrieves FTP service version).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-versions')

def nmap_snmp_community_scan(target):
    """
    Performs an SNMP community scan on the target using the '--script=snmp-communities' option (enumerates SNMP community strings).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=snmp-communities')

def nmap_ssh_version_scan(target):
    """
    Performs an SSH version scan on the target using the '--script=ssh-version' option (retrieves SSH version details).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssh-version')

def nmap_mysql_info_scan(target):
    """
    Performs a MySQL information scan on the target using the '--script=mysql-info' option (retrieves MySQL database version).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mysql-info')

def nmap_dns_zone_transfer_scan(target):
    """
    Performs a DNS zone transfer scan on the target using the '--script=dns-zone-transfer' option (attempts to retrieve DNS zone records).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dns-zone-transfer')

def nmap_pop3_vuln_scan(target):
    """
    Performs a POP3 vulnerability scan on the target using the '--script=pop3-vuln' option (checks for POP3 vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=pop3-vuln')

def nmap_telnet_vuln_scan(target):
    """
    Performs a Telnet vulnerability scan on the target using the '--script=telnet-vuln' option (checks for Telnet vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=telnet-vuln')

def nmap_imap_brute_scan(target):
    """
    Performs an IMAP brute-force scan on the target using the '--script=imap-brute' option (attempts to brute-force IMAP login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=imap-brute')

def nmap_irc_banners_scan(target):
    """
    Performs an IRC banner grabbing scan on the target using the '--script=irc-banners' option (retrieves IRC service banners).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=irc-banners')

def nmap_http_ssl_scan(target):
    """
    Performs an HTTP SSL scan on the target using the '--script=http-ssl' option (retrieves HTTP SSL certificates).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-ssl')

def nmap_smb_vuln2_scan(target):
    """
    Performs a second round of SMB vulnerability scanning using the '--script=smb-vuln-ms17-010' option (checks for MS17-010 SMB vulnerability).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-vuln-ms17-010')

def nmap_http_robots_scan(target):
    """
    Performs an HTTP robots.txt scan on the target using the '--script=http-robots' option (retrieves the robots.txt file).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-robots')

def nmap_mssql_brute_scan(target):
    """
    Performs a MSSQL brute-force scan on the target using the '--script=mssql-brute' option (attempts to brute-force MSSQL login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mssql-brute')

def nmap_smb_security_scan(target):
    """
    Performs a SMB security scan on the target using the '--script=smb-security-mode' option (checks SMB security settings).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-security-mode')

def nmap_smtp_starttls_scan(target):
    """
    Performs an SMTP STARTTLS scan on the target using the '--script=smtp-starttls' option (tests STARTTLS implementation).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-starttls')

def nmap_ftp_bypass_scan(target):
    """
    Performs an FTP bypass scan on the target using the '--script=ftp-bypass' option (checks for FTP security flaws).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-bypass')

def nmap_dhcp_server_scan(target):
    """
    Performs a DHCP server scan on the target using the '--script=dhcp-server' option (retrieves DHCP server information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dhcp-server')

def nmap_dns_traceroute_scan(target):
    """
    Performs a DNS traceroute scan on the target using the '--script=dns-traceroute' option (traces DNS query path).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dns-traceroute')

def nmap_smtp_enum_vuln_scan(target):
    """
    Performs a vulnerability scan on the SMTP server using the '--script=smtp-enum-vuln' option (detects vulnerabilities in SMTP enumeration).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-enum-vuln')

def nmap_dns_dos_scan(target):
    """
    Performs a DNS denial-of-service scan on the target using the '--script=dns-dos' option (tests DNS server robustness).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dns-dos')

def nmap_rpc_scan(target):
    """
    Performs an RPC scan on the target using the '--script=rpc-grind' option (retrieves RPC service information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=rpc-grind')

def nmap_mongodb_bypass_scan(target):
    """
    Performs a MongoDB authentication bypass scan on the target using the '--script=mongodb-bypass' option (attempts MongoDB bypass).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mongodb-bypass')

def nmap_smb_enum_shares_scan(target):
    """
    Performs an SMB share enumeration scan on the target using the '--script=smb-enum-shares' option (enumerates SMB shares).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-enum-shares')

def nmap_fingerprint_scan(target):
    """
    Performs a fingerprint scan on the target using the '--script=fingerprint' option (determines service versions).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=fingerprint')

def nmap_snmp_enum_users_scan(target):
    """
    Performs an SNMP user enumeration scan on the target using the '--script=snmp-brute' option (attempts to brute-force SNMP users).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=snmp-brute')

def nmap_ssl_certificate_scan(target):
    """
    Performs an SSL certificate scan on the target using the '--script=ssl-cert' option (retrieves SSL certificates).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssl-cert')

def nmap_dhcp_lease_scan(target):
    """
    Performs a DHCP lease scan on the target using the '--script=dhcp-lease' option (retrieves DHCP leases).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dhcp-lease')

def nmap_mysql_enum_scan(target):
    """
    Performs a MySQL enumeration scan on the target using the '--script=mysql-enum' option (enumerates MySQL users).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mysql-enum')

def nmap_http_security_scan(target):
    """
    Performs an HTTP security scan on the target using the '--script=http-security' option (checks HTTP server security).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-security')

def nmap_telnet_enum_scan(target):
    """
    Performs a Telnet enumeration scan on the target using the '--script=telnet-brute' option (attempts brute-force login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=telnet-brute')

def nmap_ftp_enumerate_scan(target):
    """
    Performs an FTP enumeration scan on the target using the '--script=ftp-enum' option (retrieves FTP user list).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-enum')
def nmap_smb_enum_users_scan(target):
    """
    Performs an SMB user enumeration scan on the target using the '--script=smb-enum-users' option (retrieves users from SMB).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-enum-users')

def nmap_pop3_enum_scan(target):
    """
    Performs a POP3 enumeration scan on the target using the '--script=pop3-brute' option (attempts to brute-force POP3 login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=pop3-brute')

def nmap_smtp_enum_scan(target):
    """
    Performs an SMTP enumeration scan on the target using the '--script=smtp-enum' option (attempts to brute-force SMTP login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-enum')

def nmap_http_cookie_scan(target):
    """
    Performs an HTTP cookie scan on the target using the '--script=http-cookie-flaw' option (checks for insecure HTTP cookies).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-cookie-flaw')

def nmap_dhcp_fingerprint_scan(target):
    """
    Performs a DHCP fingerprint scan on the target using the '--script=dhcp-fingerprint' option (retrieves DHCP server details).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dhcp-fingerprint')

def nmap_smb_enum_shares_users_scan(target):
    """
    Performs an SMB share and user enumeration scan on the target using the '--script=smb-enum-shares-users' option (retrieves SMB shares and users).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-enum-shares-users')

def nmap_ftp_version_vuln_scan(target):
    """
    Performs an FTP version vulnerability scan on the target using the '--script=ftp-vuln' option (checks for FTP version vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-vuln')

def nmap_smb_session_scan(target):
    """
    Performs an SMB session scan on the target using the '--script=smb-session' option (retrieves information on active SMB sessions).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-session')

def nmap_telnet_enumerate_scan(target):
    """
    Performs a Telnet enumeration scan on the target using the '--script=telnet-enum' option (retrieves information on Telnet sessions).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=telnet-enum')

def nmap_smtp_vuln_scan(target):
    """
    Performs an SMTP vulnerability scan on the target using the '--script=smtp-vuln' option (checks for vulnerabilities in SMTP servers).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-vuln')

def nmap_finger_scan(target):
    """
    Performs a finger scan on the target using the '--script=finger' option (checks for open finger service).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=finger')

def nmap_ftp_login_scan(target):
    """
    Performs an FTP login scan on the target using the '--script=ftp-brute' option (attempts brute-force login on FTP).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-brute')

def nmap_ssh_brute_scan(target):
    """
    Performs an SSH brute-force scan on the target using the '--script=ssh-brute' option (attempts to brute-force SSH login).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssh-brute')

def nmap_http_ssl_cc_scan(target):
    """
    Performs an HTTP SSL certificate chain scan on the target using the '--script=http-ssl-certificate' option (retrieves SSL certificate chain).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-ssl-certificate')

def nmap_smtp_starttls_vuln_scan(target):
    """
    Performs an SMTP STARTTLS vulnerability scan on the target using the '--script=smtp-starttls' option (checks for SMTP STARTTLS vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-starttls')

def nmap_https_ping_scan(target):
    """
    Performs an HTTPS ping scan on the target using the '--script=https-ping' option (checks if HTTPS server is alive).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=https-ping')

def nmap_http_user_agent_scan(target):
    """
    Performs an HTTP user-agent scan on the target using the '--script=http-user-agent' option (checks the response to user-agent variations).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-user-agent')

def nmap_http_open_redirect_scan(target):
    """
    Performs an HTTP open redirect scan on the target using the '--script=http-open-redirect' option (checks for HTTP open redirects).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-open-redirect')

def nmap_smb_domain_info_scan(target):
    """
    Performs an SMB domain information scan on the target using the '--script=smb-domain-info' option (retrieves domain information from SMB).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-domain-info')

def nmap_rdp_scan(target):
    """
    Performs an RDP (Remote Desktop Protocol) scan on the target using the '--script=rdp-vuln-ms12-020' option (checks for RDP vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=rdp-vuln-ms12-020')

def nmap_dns_recursion_scan(target):
    """
    Performs a DNS recursion scan on the target using the '--script=dns-recursion' option (checks for DNS recursion support).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dns-recursion')

def nmap_http_ssl_scan(target):
    """
    Performs an SSL scan on the target using the '--script=http-ssl' option (checks for SSL support and certificates).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-ssl')

def nmap_mongodb_auth_scan(target):
    """
    Performs a MongoDB authentication scan on the target using the '--script=mongodb-auth' option (checks MongoDB for authentication vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mongodb-auth')

def nmap_http_basic_auth_brute_scan(target):
    """
    Performs an HTTP basic authentication brute-force scan on the target using the '--script=http-brute' option (attempts to brute-force HTTP basic auth).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=http-brute')

def nmap_ftp_vuln_scan(target):
    """
    Performs an FTP vulnerability scan on the target using the '--script=ftp-vuln' option (checks FTP for known vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ftp-vuln')

def nmap_snmp_enumerate_users_scan(target):
    """
    Performs an SNMP user enumeration scan on the target using the '--script=snmp-brute' option (retrieves SNMP users).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=snmp-brute')

def nmap_ssl_scan(target):
    """
    Performs an SSL scan on the target using the '--script=ssl-enum-ciphers' option (lists supported SSL ciphers).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=ssl-enum-ciphers')

def nmap_netbios_scan(target):
    """
    Performs a NetBIOS scan on the target using the '--script=nbstat' option (retrieves NetBIOS information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=nbstat')

def nmap_mysql_enum_vuln_scan(target):
    """
    Performs a MySQL enumeration vulnerability scan on the target using the '--script=mysql-vuln' option (checks for MySQL vulnerabilities).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=mysql-vuln')

def nmap_dns_scan(target):
    """
    Performs a DNS scan on the target using the '--script=dns-scan' option (checks DNS information).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=dns-scan')

def nmap_fingerprint_scan(target):
    """
    Performs a fingerprint scan on the target using the '--script=fingerprint' option (identifies services and their versions).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=fingerprint')

def nmap_smb_enum_machine_scan(target):
    """
    Performs an SMB machine enumeration scan on the target using the '--script=smb-enum-machines' option (retrieves machines on the SMB network).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smb-enum-machines')

def nmap_smtp_tls_vuln_scan(target):
    """
    Performs an SMTP TLS vulnerability scan on the target using the '--script=smtp-tls' option (checks for vulnerabilities in SMTP over TLS).
    
    Args:
        target (str): The IP address or hostname to scan.
    """
    nmap_scan(target, '--script=smtp-tls')
