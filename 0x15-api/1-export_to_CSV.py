#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Salam Qadri
"""
from requests import get
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = get(user_url)
    user_username = user_response.json().get('username')

    todos_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    todos_response = get(todos_url)
    todos_list = todos_response.json()

    with open('{}.csv'.format(user_id), 'w') as output_file:
        for todo in todos_list:
            output_file.write('"{}","{}","{}","{}"\n'
                              .format(user_id, user_username, todo.get('completed'),
                                      todo.get('title')))
