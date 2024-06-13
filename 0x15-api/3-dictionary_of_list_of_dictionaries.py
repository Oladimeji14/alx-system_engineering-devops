#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Salam Qadri
"""
from json import dump
from requests import get


if __name__ == '__main__':
    url_base = 'https://jsonplaceholder.typicode.com/users/'
    response_users = get(url_base)
    users = response_users.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url_todos = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
        response_todos = get(url_todos)
        tasks = response_todos.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })
    with open('todo_all_employees.json', 'w') as file:
        dump(dictionary, file)
