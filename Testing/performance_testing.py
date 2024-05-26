from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def load_home(self):
        self.client.get("/")

    @task
    def load_login(self):
        self.client.get("/login")

    @task
    def login(self):
        self.client.post("/login", data={"username": "testuser", "password": "testpass"})

    @task
    def load_signup(self):
        self.client.get("/signup")

    @task
    def signup(self):
        self.client.post("/signup", data={"username": "newuser", "password": "newpass"})

    @task
    def load_predict(self):
        self.client.get("/predict")

    @task
    def predict(self):
        self.client.post("/predict", data={"longitude": "80.2707", "latitude": "13.0827"})
