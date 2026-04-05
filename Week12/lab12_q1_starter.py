import socket
import urllib.request
import urllib.error


class Scanner:
    def __init__(self, target):
        self.target = target
        self.results = []

    def display_results(self):
        print(f"\nResults for {self.target}:")
        if not self.results:
            print("No results found.")
        else:
            for result in self.results:
                print(result)


class PortScanner(Scanner):
    def __init__(self, target, ports):
        super().__init__(target)
        self.ports = ports

    def scan(self):
        for port in self.ports:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                result = sock.connect_ex((self.target, port))

                if result == 0:
                    self.results.append(f"Port {port} is OPEN")
                else:
                    self.results.append(f"Port {port} is CLOSED")

                sock.close()
            except Exception as e:
                self.results.append(f"Port {port} error: {e}")


class HTTPScanner(Scanner):
    def __init__(self, target, paths):
        super().__init__(target)
        self.paths = paths

    def scan(self):
        for path in self.paths:
            url = self.target.rstrip("/") + "/" + path.lstrip("/")
            try:
                response = urllib.request.urlopen(url, timeout=3)
                self.results.append(f"{url} -> Status {response.status}")
            except urllib.error.HTTPError as e:
                self.results.append(f"{url} -> HTTP Error {e.code}")
            except urllib.error.URLError as e:
                self.results.append(f"{url} -> URL Error: {e.reason}")
            except Exception as e:
                self.results.append(f"{url} -> Error: {e}")


if __name__ == "__main__":
    print("=== Port Scanner ===")
    port_scanner = PortScanner("scanme.nmap.org", [21, 22, 80, 443])
    port_scanner.scan()
    port_scanner.display_results()

    print("\n=== HTTP Scanner ===")
    http_scanner = HTTPScanner("http://example.com", ["", "about", "test"])
    http_scanner.scan()
    http_scanner.display_results()