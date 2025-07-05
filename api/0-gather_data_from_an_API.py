#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    emp_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

    try:
        user_resp = requests.get(user_url)
        todos_resp = requests.get(todos_url)
        user_resp.raise_for_status()
        todos_resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    user = user_resp.json()
    todos = todos_resp.json()

    name = user.get("name")
    total = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]
    done_count = len(done_tasks)

    print(f"Employee {name} is done with tasks({done_count}/{total}):")
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
