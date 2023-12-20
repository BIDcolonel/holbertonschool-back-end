#!/usr/bin/python3
"""Script that save in csv infos from a given employee"""

import csv
import requests
import sys


API_URL = 'https://jsonplaceholder.typicode.com'


def get_user_info(user_id):
    user_info = requests.get(f'{API_URL}/users/{user_id}').json()
    return user_info


def get_user_tasks(user_id):
    tasks = requests.get(f"{API_URL}/todos?userId={user_id}").json()
    return tasks


def export_to_csv(user, tasks, filename):
    with open(filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in tasks:
            csv_writer.writerow([
                user['id'],
                user['username'],
                task['completed'],
                task['title']
            ])


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the user ID as an argument.")
        sys.exit(1)

    user_id = sys.argv[1]

    user_info = get_user_info(user_id)
    user_tasks = get_user_tasks(user_id)

    csv_filename = f"{user_id}.csv"
    export_to_csv(user_info, user_tasks, csv_filename)

    print(f"Data has been exported to {csv_filename}")
