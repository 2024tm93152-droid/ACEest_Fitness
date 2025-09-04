from flask import Flask, jsonify, request
from ACEest_Fitness import WorkoutManager

app = Flask(__name__)
manager = WorkoutManager()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to ACEest Fitness API!"}), 200

@app.route("/workout", methods=["POST"])
def add_workout():
    data = request.get_json()
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or not duration:
        return jsonify({"error": "Missing workout or duration"}), 400

    new_workout = manager.add_workout(workout, duration)
    return jsonify({"status": "success", "workout": new_workout}), 201

@app.route("/workouts", methods=["GET"])
def get_workouts():
    return jsonify({"workouts": manager.get_workouts()}), 200

if __name__ == "__main__": # pragma: no cover
    app.run(host="0.0.0.0", port=5000)