
# QA Test Project

## Setup and Run Instructions

### Prerequisites
- Minikube
- kubectl
- Python3
- requests library

### Steps to Deploy Services

1. **Start Minikube:**
   ```sh
   minikube start
   ```

2. **Clone the Repository:**
   ```sh
   git clone https://github.com/Vengatesh-m/qa-test.git
   cd qa-test
   ```

3. **Apply the Deployments:**
   ```sh
   kubectl apply -f backend-deployment.yaml
   kubectl apply -f frontend-deployment.yaml
   ```

4. **Expose Services:**
   ```sh
   kubectl expose deployment frontend --type=LoadBalancer --port=80
   kubectl expose deployment backend --type=ClusterIP --port=5000
   ```

5. **Check Service Status:**
   ```sh
   kubectl get services
   ```

6. **Access Frontend URL:**
   Use the Minikube IP and the frontend service port to access the frontend URL. Verify that it displays the greeting message fetched from the backend.

### Running the Automated Test Script

1. **Install Python Requirements:**
   ```sh
   pip install requests
   ```

2. **Run the Test Script:**
   ```sh
   python test_integration.py
   ```

## Expected Result
- The test should pass, verifying that the frontend correctly displays the message returned by the backend.
