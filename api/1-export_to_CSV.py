#!/usr/bin/python3
"""
1-export_to_CSV.py

Exports all TODO tasks for a given employee ID from the JSONPlaceholder API
to a CSV file in the following format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetch user info and tasks list for the specified employee ID.

    Returns:
        user_data (dict): JSON response with employee information.
        todos (list): List of tasks associated with the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_resp = requests.get(user_url)
    todos_resp = requests.get(todos_url)
    user_resp.raise_for_status()
    todos_resp.raise_for_status()

    return user_resp.json(), todos_resp.json()


def export_tasks_to_csv(user, todos):
    """
    Write employee's task data into a CSV file.

    Args:
        user (dict): Employee information.
        todos (list): List of all tasks.
    """
    user_id = user.get("id")
    username = user.get("username")
    filename = f"{user_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    try:
        user_info, task_list = fetch_employee_data(employee_id)
        export_tasks_to_csv(user_info, task_list)
    except requests.RequestException as error:
        print(f"Error fetching data: {error}")
        sys.exit(1)
