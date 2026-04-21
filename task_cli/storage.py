# This file handles ALL reading and writing of tasks.json
# No other file should touch the JSON file directly

import json
import os

# The name of our database file
TASKS_FILE = "tasks.json"


"""READ ALL TASKS FROM THE JSON FILE AND RETURN AS A LIST"""
def load_tasks():
    # If the file doesn't exist yet, create it with an empty list
    if not os.path.exists(TASKS_FILE):
        save_tasks([])

    # Open the file and read it
    with open(TASKS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("Error: tasks.json is corrupted. Starting fresh.")
            return []
        

"""write the full tasks list to the JSON file"""
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

"""Return the next available task ID."""
def get_next_di(tasks):
    # If no tasks exist, start from ID 1
    if not tasks:
        return 1
    # Otherwise take the highest existing ID and add 1
    return max(task["id"] for task in tasks) + 1


def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None