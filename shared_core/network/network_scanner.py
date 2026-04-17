import nmap

class NetworkScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()

    def scan_network(self, subnet="192.168.1.0/24"):
        self.nm.scan(hosts=subnet, arguments="-sn")
        devices = {}
        for host in self.nm.all_hosts():
            devices[host] = {
                "mac": self.nm[host]["addresses"].get("mac", "Unknown"),
                "vendor": self.nm[host]["vendor"],
                "status": self.nm[host]["status"]["state"]
            }
        return devices