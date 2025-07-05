#!/usr/bin/python3
"""
2-export_to_JSON.py

Fetches all TODO tasks for a given employee ID from the JSONPlaceholder API,
and exports them to a JSON file in the format:

{
  "USER_ID": [
    {
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS,
      "username": "USERNAME"
    },
    ...
  ]
}
"""

import json
import requests
import sys


def fetch_user_and_tasks(user_id):
    """Fetch employee info and task list for given ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{user_id}"
    todos_url = f"{base_url}/todos?userId={user_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    user_response.raise_for_status()
    todos_response.raise_for_status()

    return user_response.json(), todos_response.json()


def export_tasks_to_json(user, tasks):
    """Export user tasks to a JSON file named USER_ID.json."""
    user_id = str(user.get("id"))
    username = user.get("username")

    task_list = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in tasks
    ]

    filename = f"{user_id}.json"
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump({user_id: task_list}, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    try:
        user_data, todos_data = fetch_user_and_tasks(user_id)
        export_tasks_to_json(user_data, todos_data)
    except requests.RequestException as error:
        print(f"Request failed: {error}")
        sys.exit(1)
