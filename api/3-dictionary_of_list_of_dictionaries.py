#!/usr/bin/python3
"""Script that save in csv infos from a given employee"""

import json
import requests


API_URL = 'https://jsonplaceholder.typicode.com'


def get_users():
    """Get users from the API"""
    response = requests.get(f'{API_URL}/users')
    return response.json()


def get_todos():
    """Get todos from the API"""
    response = requests.get(f"{API_URL}/todos")
    return response.json()


def organize_data(users, todos):
    """Organize data based on users and tasks"""
    data = {}

    for task in todos:
        user_id = task['userId']

        if user_id not in data:
            data[user_id] = []

        data[user_id].append({
            "username": next(user['username']
                             for user in users
                             if user['id'] == user_id),
            "task": task['title'],
            "completed": task['completed']
        })

    return data


def save_to_json(data, filename):
    """Save data to a JSON file"""
    with open(filename, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    users = get_users()
    todos = get_todos()
    json_filename = "todo_all_employees.json"
    organized_data = organize_data(users, todos)
    save_to_json(organized_data, json_filename)
