#!/usr/bin/python3
"""Python script using  API"""


import requests
import sys


def gather_data():
    """display on the standard output the employee TODO list progress """
    userId = sys.argv[1]
    users_route = 'https://jsonplaceholder.typicode.com/users/{}'
    todos_route = 'https://jsonplaceholder.typicode.com/todos/?userId={}'
    user = users_route.format(userId)
    todos = todos_route.format(userId)
    name = requests.get(user).json().get('name')
    todos_request = requests.get(todos).json()
    tasks = [task.get('title') for task in todos_request
             if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(name,
          len(tasks), len(todos_request)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        gather_data()