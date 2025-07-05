#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Fetches and displays the TODO list progress for a given employee ID
using the JSONPlaceholder REST API.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch user and task data for the given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    user_response.raise_for_status()
    todos_response.raise_for_status()

    return user_response.json(), todos_response.json()


def display_task_summary(user, tasks):
    """Print the TODO summary and completed task titles."""
    name = user.get("name")
    total_tasks = len(tasks)
    done_tasks = [task for task in tasks if task.get("completed") is True]
    done_count = len(done_tasks)

    print(f"Employee {name} is done with tasks({done_count}/{total_tasks}):")
    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        user_data, todos_data = fetch_employee_data(employee_id)
        display_task_summary(user_data, todos_data)
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
