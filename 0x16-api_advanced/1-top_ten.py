#!/usr/bin/python3
"""
@author: Salam Qadri
"""
from json import loads
from requests import get


def fetch_top_ten_posts(community):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    api_endpoint = 'https://www.reddit.com/r/{}/hot.json'.format(community)
    request_headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    api_response = get(api_endpoint, headers=request_headers, allow_redirects=False)
    response_data = api_response.json()

    try:
        post_list = response_data.get('data').get('children')
        for idx in range(10):
            print(post_list[idx].get('data').get('title'))
    except:
        print('None')
