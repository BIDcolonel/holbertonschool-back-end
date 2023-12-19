#!/usr/bin/python3
"""Script that display infos for a given employee"""

import requests
import sys


users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_tasks(id):
    """ Fetch user name, number of tasks """
    user_resp = requests.get(f"{users_url}/{id}").json()
    employee_name = user_resp['name']

    todos_resp = requests.get(f"{todos_url}?userId={id}").json()
    total_tasks = len(todos_resp)
    completed_tasks = [task for task in todos_resp if task['completed']]

    output_str = (
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{total_tasks}):\n"
    )
    print(output_str)

    for task in completed_tasks:
        task_str = f"\t {task['title']}"
        print(task_str)

    output_filename = 'student_output'
    with open(output_filename, 'w') as output_file:
        count = 0
        for task in completed_tasks:
            count += 1
            task_str = f"\t {task['title']}\n"
            if task_str[0] == '\t' and task_str[-1] == '\n':
                output_file.write(f"Task {count} Formatting: OK\n")
            else:
                output_file.write(f"Task {count} Formatting: Incorrect\n")


if __name__ == "__main__":
    check_tasks(int(sys.argv[1]))
