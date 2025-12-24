"""
Configuration for Locust performance tests
Defines test parameters and thresholds
"""

# API Configuration
BASE_URL = "https://jsonplaceholder.typicode.com"

# Load Test Configuration
LOAD_TEST = {
    "users": 50,
    "spawn_rate": 5,
    "duration": "5m",
    "description": "Gradual load increase to establish baseline"
}

# Stress Test Configuration
STRESS_TEST = {
    "users": 100,
    "spawn_rate": 10,
    "duration": "4m",
    "description": "Find system breaking point under heavy load"
}

# Spike Test Configuration
SPIKE_TEST = {
    "max_users": 200,
    "min_users": 10,
    "duration": "4m",
    "description": "Test recovery from sudden traffic spikes"
}

# Performance Thresholds
THRESHOLDS = {
    "p50": 200,   # 50th percentile - 200ms
    "p95": 500,   # 95th percentile - 500ms
    "p99": 1000   # 99th percentile - 1000ms
}

# Error Rate Threshold
MAX_ERROR_RATE = 1.0  # Maximum acceptable error rate (1%)

# Response Time Grades
PERFORMANCE_GRADES = {
    "excellent": {"max_p95": 200},
    "good": {"max_p95": 500},
    "fair": {"max_p95": 1000},
    "poor": {"max_p95": float('inf')}
}
