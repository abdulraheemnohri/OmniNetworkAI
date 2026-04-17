from network.network_scanner import NetworkScanner

class DeviceDiscovery:
    def __init__(self):
        self.scanner = NetworkScanner()
        self.devices = {}

    def discover_devices(self, subnet="192.168.1.0/24"):
        new_devices = self.scanner.scan_network(subnet)
        self.devices.update(new_devices)
        return self.devices

    def get_device_info(self, ip):
        return self.devices.get(ip, "Device not found")

    def list_all_devices(self):
        return self.devices
