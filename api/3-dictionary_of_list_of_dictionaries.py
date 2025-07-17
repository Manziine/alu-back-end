#!/usr/bin/python3
"""Export JSON"""

import json
import requests


def get_todos(user_id):
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    response = requests.get(url)
    return json.loads(response.text)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url)
    users = json.loads(response.text)

    data = {}
    for user in users:
        todos = get_todos(user["id"])
        data[user["id"]] = [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            }
            for todo in todos
        ]

    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data))
