# ACEest_Fitness.py

class WorkoutManager:
    def __init__(self):
        self.workouts = []

    def add_workout(self, workout, duration):
        self.workouts.append({"workout": workout, "duration": duration})
        return self.workouts[-1]

    def get_workouts(self):
        return self.workouts


# Optional Tkinter GUI (only runs locally, not in Docker/CI)
if __name__ == "__main__":
    import tkinter as tk
    from tkinter import messagebox

    class FitnessTrackerApp:
        def __init__(self, master, manager):
            self.master = master
            self.manager = manager
            master.title("ACEestFitness and Gym")

            # Labels and Entries
            self.workout_label = tk.Label(master, text="Workout:")
            self.workout_label.grid(row=0, column=0, padx=5, pady=5)
            self.workout_entry = tk.Entry(master)
            self.workout_entry.grid(row=0, column=1, padx=5, pady=5)

            self.duration_label = tk.Label(master, text="Duration (minutes):")
            self.duration_label.grid(row=1, column=0, padx=5, pady=5)
            self.duration_entry = tk.Entry(master)
            self.duration_entry.grid(row=1, column=1, padx=5, pady=5)

            # Buttons
            self.add_button = tk.Button(master, text="Add Workout", command=self.add_workout)
            self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

            self.view_button = tk.Button(master, text="View Workouts", command=self.view_workouts)
            self.view_button.grid(row=3, column=0, columnspan=2, pady=10)

        def add_workout(self):
            workout = self.workout_entry.get()
            duration = self.duration_entry.get()

            if workout and duration:
                self.manager.add_workout(workout, duration)
                messagebox.showinfo("Success", "Workout added successfully!")
            else:
                messagebox.showwarning("Input Error", "Please enter both workout and duration.")

        def view_workouts(self):
            workouts = self.manager.get_workouts()
            if workouts:
                workout_list = "\n".join([f"{w['workout']} - {w['duration']} min" for w in workouts])
                messagebox.showinfo("Workouts", workout_list)
            else:
                messagebox.showinfo("Workouts", "No workouts recorded.")

    root = tk.Tk()
    manager = WorkoutManager()
    app = FitnessTrackerApp(root, manager)
    root.mainloop()