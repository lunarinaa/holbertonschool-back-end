#!/usr/bin/python3
"""Exports data in CSV  format"""

import csv
import requests
from sys import argv


def export_data():
    """method to export related data"""
    users_route = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_route = 'https://jsonplaceholder.typicode.com/todos/?userID={}'
    users = users_route.format(argv[1])
    todos = todos_route.format(argv[1])
    username = requests.get(users).json().get('username')
    todos_request = requests.get(todos).json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        for todo in todos_request:
            save = '"{}", "{}", "{}", "{}"\n'.format(
                argv[1], username, todo.get('completed'), todo.get('title'))
            file.write(save)


if __name__ == "__main__":
    export_data()
