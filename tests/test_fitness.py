import pytest
from ACEest_Fitness import WorkoutManager

def test_add_single_workout():
    manager = WorkoutManager()
    result = manager.add_workout("Running", 30)
    assert result == {"workout": "Running", "duration": 30}
    assert len(manager.get_workouts()) == 1

def test_add_multiple_workouts():
    manager = WorkoutManager()
    manager.add_workout("Running", 30)
    manager.add_workout("Cycling", 45)
    workouts = manager.get_workouts()
    assert len(workouts) == 2
    assert workouts[0]["workout"] == "Running"
    assert workouts[1]["duration"] == 45

def test_get_workouts_initially_empty():
    manager = WorkoutManager()
    assert manager.get_workouts() == []