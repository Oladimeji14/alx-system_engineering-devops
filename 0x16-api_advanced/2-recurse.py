#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@author: Salam Qadri
"""
import json
import requests


def fetch_hot_posts(subreddit, post_list=[]):
    """Recursively fetches titles of hot articles from a specified subreddit using the Reddit API.
    If no results are found, the function returns None.
    """
    api_url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        'User-Agent': 'Python/requests: API Client'
    }

    try:
        response = requests.get(api_url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        posts = data.get('data', {}).get('children', [])
        if not posts:
            print(None)
            return None

        for post in posts:
            post_list.append(post.get('data', {}).get('title', 'No Title'))

        return post_list
    except requests.RequestException as e:
        print(f"Error: {e}")
        print(None)
        return None
