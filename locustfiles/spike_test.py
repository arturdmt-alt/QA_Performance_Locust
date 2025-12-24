from locust import HttpUser, task, between, LoadTestShape

class SpikeTestUser(HttpUser):
    """User behavior for spike testing"""
    host = "https://jsonplaceholder.typicode.com"
    wait_time = between(1, 2)
    
    @task
    def get_data(self):
        self.client.get("/users")

class SpikeShape(LoadTestShape):
    """
    Spike pattern: Low → High → Low → High
    Tests system recovery after traffic spikes
    """
    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 120, "users": 200, "spawn_rate": 50},
        {"duration": 180, "users": 10, "spawn_rate": 50},
        {"duration": 240, "users": 200, "spawn_rate": 50},
    ]
    
    def tick(self):
        run_time = self.get_run_time()
        
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        
        return None
    