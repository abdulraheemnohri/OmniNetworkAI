import cv2

class RTSPStream:
    def __init__(self, url):
        self.url = url

    def capture_frame(self, output_path="frame.jpg"):
        try:
            cap = cv2.VideoCapture(self.url)
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(output_path, frame)
                cap.release()
                return f"Frame captured to {output_path}"
            cap.release()
            return "Failed to capture frame"
        except Exception as e:
            return f"RTSP Error: {e}"

    def detect_motion(self, duration=5):
        # Placeholder for motion detection logic
        return "Motion detected" if duration > 0 else "No motion"
