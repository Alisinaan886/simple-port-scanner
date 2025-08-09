import socket
import sys
from datetime import datetime

def get_own_ip():
    """Get the current machine's local IP address."""
    try:
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    except:
        return "127.0.0.1"  # fallback

def scan_ports(target_ip, start_port, end_port):
    print(f"\n[+] Scanning Target: {target_ip}")
    print(f"[+] Time Started: {datetime.now()}")
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Timeout for each port
            result = s.connect_ex((target_ip, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
            s.close()
    except KeyboardInterrupt:
        print("\n[-] Scan interrupted by user.")
        sys.exit()
    except socket.gaierror:
        print("[-] Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("[-] Could not connect to server.")
        sys.exit()

    print("-" * 50)
    print(f"[+] Scan Completed at: {datetime.now()}")

if __name__ == "__main__":
    print("=== Simple Python Port Scanner ===")
    own_ip = get_own_ip()
    print(f"Your detected IP address is: {own_ip}")
    
    choice = input("Do you want to scan your own IP? (y/n): ").strip().lower()
    if choice == 'y':
        target = own_ip
    else:
        target = input("Enter target IP address: ")

    start = int(input("Enter starting port: "))
    end = int(input("Enter ending port: "))

    scan_ports(target, start, end)
