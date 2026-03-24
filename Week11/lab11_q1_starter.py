print("RUNNING Q1")

import socket


class PortScanner:
    def __init__(self, target):
        self.target = target
        self.open_ports = []

    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((self.target, port))
            if result == 0:
                print(f"  Port {port}: OPEN")
                self.open_ports.append(port)
                return True
            return False
        finally:
            sock.close()

    def scan_range(self, start_port, end_port):
        for port in range(start_port, end_port + 1):
            self.scan_port(port)

    def display_results(self):
        print(f"  Results for {self.target}:")
        if len(self.open_ports) == 0:
            print("    No open ports found.")
        else:
            for port in self.open_ports:
                print(f"    Port {port}")


if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: PORT SCANNER CLASS")
    print("=" * 60)

    print("\n--- Scanner 1: localhost ---")
    scanner1 = PortScanner("127.0.0.1")
    print("  Scanning 127.0.0.1 ports 78-82...")
    scanner1.scan_range(78, 82)
    scanner1.display_results()

    print("\n--- Scanner 2: different target ---")
    scanner2 = PortScanner("127.0.0.1")
    print("  Scanning 127.0.0.1 ports 20-25...")
    scanner2.scan_range(20, 25)
    scanner2.display_results()

    print("\n" + "=" * 60)