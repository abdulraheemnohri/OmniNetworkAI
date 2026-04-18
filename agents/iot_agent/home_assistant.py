import requests

class HomeAssistantClient:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def get_state(self, entity_id):
        response = requests.get(f"{self.url}/api/states/{entity_id}", headers=self.headers)
        return response.json()

    def call_service(self, domain, service, entity_id, data=None):
        payload = {"entity_id": entity_id}
        if data:
            payload.update(data)
        response = requests.post(f"{self.url}/api/services/{domain}/{service}",
                                 headers=self.headers, json=payload)
        return response.json()
