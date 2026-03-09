import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}")

def main():
    target = input("Enter target IP address: ")
    print(f"\nScanning target: {target}")
    print("Scanning started at:", datetime.now())
    print("-" * 50)
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in common_ports:
            executor.submit(scan_port, target, port)

    print("-" * 50)
    print("Scan complete at:", datetime.now())

if __name__ == "__main__":
    main()