from locust import HttpUser, task, between, events
import logging

class StressTestUser(HttpUser):
    """
    Stress test to find breaking point
    Increases load until system fails
    """
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(0.5, 1)
    
    @task
    def stress_endpoint(self):
        """Heavy load on /users endpoint"""
        with self.client.get("/users", catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Status: {response.status_code}")
            elif response.elapsed.total_seconds() > 2:
                response.failure(f"Too slow: {response.elapsed.total_seconds()}s")

@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    logging.info("Stress test starting - finding breaking point")

@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    logging.info("Stress test completed")
    