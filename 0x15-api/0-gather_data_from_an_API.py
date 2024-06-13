#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Salam Qadri
"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    user_info_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    user_response = requests.get(user_info_url)
    user_name = user_response.json().get('name')

    todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    
    completed_count = 0
    completed_tasks = []

    for todo in todos:
        if todo.get('completed'):
            completed_tasks.append(todo)
            completed_count += 1

    print(f"Employee {user_name} has completed tasks ({completed_count}/{len(todos)}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
