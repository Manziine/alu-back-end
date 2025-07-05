#!/usr/bin/python3
"""
1-export_to_CSV.py

Exports all TODO tasks for a given employee ID from the JSONPlaceholder API
to a CSV file in the format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys


def fetch_user_and_tasks(employee_id):
    """Fetches user details and their tasks from JSONPlaceholder."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    user_response.raise_for_status()
    todos_response.raise_for_status()

    return user_response.json(), todos_response.json()


def export_to_csv(user, todos):
    """Writes the employee's task data to a CSV file."""
    filename = f"{user['id']}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user['id'],
                user['username'],
                str(task['completed']),
                task['title']
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    try:
        user, todos = fetch_user_and_tasks(employee_id)
        export_to_csv(user, todos)
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
