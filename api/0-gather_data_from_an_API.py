#!/usr/bin/python3
"""Script that display infos for a given employee"""

import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Make a GET request to the API
response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")

if response.status_code != 200:
    print("Error: Employee not found")
    sys.exit(1)

employee_data = response.json()
employee_name = employee_data["name"]

# Make a GET request to the API to get the employee's TODO list
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

if response.status_code != 200:
    print("Error: Failed to fetch TODO list")
    sys.exit(1)

todos = response.json()
total_tasks = len(todos)
completed_tasks = [todo for todo in todos if todo["completed"]]

print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
for task in completed_tasks:
    print(f"\t{task['title']}")
