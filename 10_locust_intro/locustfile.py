from locust import HttpUser, between ,task

class HitCounterUser(HttpUser):
    """
    Simulates a user interacting with the Hit Counter app.
    """
    host = "http://localhost:5000"
    wait_time = between(3, 5)
    
    @task(1)
    def load_homepage(self):
        self.client.get("/")

    @task(3) #Semakin tinggi angkanya semakin sering dilakukan tasknya
    def post_hit(self):
        self.client.post("/hit")