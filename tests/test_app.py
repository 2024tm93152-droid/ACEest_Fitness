from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Welcome to ACEest Fitness API!"

def test_add_workout():
    client = app.test_client()
    response = client.post("/workout", json={"workout": "Running", "duration": 30})
    assert response.status_code == 201
    data = response.get_json()
    assert data["status"] == "success"
    assert data["workout"]["workout"] == "Running"

def test_get_workouts():
    client = app.test_client()
    client.post("/workout", json={"workout": "Cycling", "duration": 45})
    response = client.get("/workouts")
    assert response.status_code == 200
    data = response.get_json()
    assert "workouts" in data
    assert isinstance(data["workouts"], list)