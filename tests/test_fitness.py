import pytest
from ACEest_Fitness import WorkoutManager

def test_add_and_get_single_workout():
    manager = WorkoutManager()
    result = manager.add_workout("Running", 30)
    assert result == {"workout": "Running", "duration": 30}
    workouts = manager.get_workouts()
    assert len(workouts) == 1
    assert workouts[0]["workout"] == "Running"

def test_add_multiple_workouts():
    manager = WorkoutManager()
    manager.add_workout("Cycling", 45)
    manager.add_workout("Yoga", 60)
    workouts = manager.get_workouts()
    assert len(workouts) == 2
    assert workouts[0]["workout"] == "Cycling"
    assert workouts[1]["duration"] == 60

def test_get_workouts_initially_empty():
    manager = WorkoutManager()
    assert manager.get_workouts() == []

def test_add_invalid_data_types():
    manager = WorkoutManager()
    # Duration as string (still accepted, but check behavior)
    result = manager.add_workout("Swimming", "thirty")
    assert result["duration"] == "thirty"
    assert isinstance(manager.get_workouts(), list)