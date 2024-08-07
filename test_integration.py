
import requests

def test_integration():
    frontend_url = "http://<minikube_ip>:<frontend_port>"
    response = requests.get(frontend_url)
    assert response.status_code == 200
    assert "Hello from backend" in response.text

if __name__ == "__main__":
    test_integration()
