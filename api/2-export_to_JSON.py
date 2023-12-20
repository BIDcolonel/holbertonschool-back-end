#!/usr/bin/python3
"""Script that saves info from a given employee in a CSV file"""

import json
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'


def get_user_info(user_id):
    """Get user information"""
    user = requests.get(f'{API_URL}/users/{user_id}').json()
    return user


def get_user_todos(user_id):
    """Get user's to-do list"""
    todo_list = requests.get(f"{API_URL}/todos?userId={user_id}").json()
    return todo_list


def create_data(user, todo_list, user_id):
    """Create data structure"""
    data = {
        user_id: [
            {
                "task": task['title'],
                "completed": task['completed'],
                "username": user['username']
            }
            for task in todo_list
        ]
    }
    return data


def save_to_json(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    USER_ID = sys.argv[1]

    user_info = get_user_info(USER_ID)
    user_todos = get_user_todos(USER_ID)
    json_filename = f"{USER_ID}.json"

    data = create_data(user_info, user_todos, USER_ID)
    save_to_json(data, json_filename)
