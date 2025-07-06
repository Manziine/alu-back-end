#!/usr/bin/python3
"""
Exports all employees' TODO tasks to a JSON file.
"""

import json
import requests


def export_all_tasks_to_json():
    """Export all employees' tasks to a JSON file."""
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Get all users
    users_response = requests.get(f"{base_url}/users")
    users = users_response.json()

    # Get all todos
    todos_response = requests.get(f"{base_url}/todos")
    todos = todos_response.json()

    # Create a dictionary to hold all tasks organized by user ID
    all_tasks = {}

    for user in users:
        user_id = user["id"]
        username = user["username"]
        
        # Filter todos for this user
        user_todos = [todo for todo in todos if todo["userId"] == user_id]
        
        # Format the tasks for this user
        tasks_list = []
        for todo in user_todos:
            task_dict = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            tasks_list.append(task_dict)
        
        # Add to the main dictionary
        all_tasks[str(user_id)] = tasks_list

    # Write to JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_tasks, jsonfile, indent=4)


if __name__ == "__main__":
    export_all_tasks_to_json() 
