import socket
from datetime import datetime

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
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

    for port in common_ports:
        scan_port(target, port)

if __name__ == "__main__":
    main()