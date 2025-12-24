from locust import HttpUser, task, between

class APIUser(HttpUser):
    """
    Basic load test for JSONPlaceholder API
    Simulates users making GET and POST requests
    """
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 3)  # Random wait between requests
    
    @task(3)
    def get_users(self):
        """GET /users - weight 3 (most frequent)"""
        with self.client.get("/users", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Got status {response.status_code}")
    
    @task(2)
    def get_posts(self):
        """GET /posts - weight 2"""
        with self.client.get("/posts", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Got status {response.status_code}")
    
    @task(1)
    def create_post(self):
        """POST /posts - weight 1 (least frequent)"""
        payload = {
            "title": "Performance Test Post",
            "body": "Testing API performance",
            "userId": 1
        }
        with self.client.post("/posts", json=payload, catch_response=True) as response:
            if response.status_code not in [200, 201]:
                response.failure(f"Got status {response.status_code}")
                