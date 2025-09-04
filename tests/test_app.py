import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Welcome to ACEest Fitness API!"

def test_add_workout_success(client):
    response = client.post("/workout", json={"workout": "Running", "duration": 30})
    data = response.get_json()
    assert response.status_code == 201
    assert data["status"] == "success"
    assert data["workout"]["workout"] == "Running"
    assert data["workout"]["duration"] == 30

def test_add_workout_missing_fields(client):
    # Missing duration
    response = client.post("/workout", json={"workout": "Swimming"})
    assert response.status_code == 400
    assert "error" in response.get_json()

    # Missing workout
    response = client.post("/workout", json={"duration": 20})
    assert response.status_code == 400
    assert "error" in response.get_json()

def test_add_workout_invalid_json(client):
    # Sending text instead of JSON
    response = client.post("/workout", data="notjson", content_type="text/plain")
    assert response.status_code in (400, 415)  # Flask may throw BadRequest or Unsupported Media Type

def test_get_workouts_after_adding(client):
    client.post("/workout", json={"workout": "Cycling", "duration": 45})
    client.post("/workout", json={"workout": "Yoga", "duration": 60})

    response = client.get("/workouts")
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data["workouts"], list)
    assert len(data["workouts"]) >= 2
    assert any(w["workout"] == "Cycling" for w in data["workouts"])
    assert any(w["workout"] == "Yoga" for w in data["workouts"])

def test_invalid_http_methods(client):
    # Using PUT instead of POST
    response = client.put("/workout", json={"workout": "Boxing", "duration": 20})
    assert response.status_code in (405, 404)  # Method Not Allowed or Not Found

    # Using DELETE instead of GET
    response = client.delete("/workouts")
    assert response.status_code in (405, 404)