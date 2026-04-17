class ONVIFClient:
    def __init__(self, ip=None, user=None, password=None):
        self.ip = ip
        self.user = user
        self.password = password

    def get_camera_list(self):
        # Mocking ONVIF discovery
        return [{"id": "cam_01", "name": "Front Gate", "ip": "192.168.1.50"}, {"id": "cam_02", "name": "Backyard", "ip": "192.168.1.51"}]

    def reboot_camera(self, camera_id):
        return f"Camera {camera_id} rebooted."
