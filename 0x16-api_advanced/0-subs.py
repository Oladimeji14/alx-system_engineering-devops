#!/usr/bin/python3
# -*- coding: utf-8 -*-
from json import loads
from requests import get


def get_subscriber_count(community):
    """Recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return None
    """
    api_url = 'https://www.reddit.com/r/{}/about.json'.format(community)
    request_headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) \
        Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)'
    }
    api_response = get(api_url, headers=request_headers)
    response_data = api_response.json()

    try:
        subscriber_count = response_data.get('data').get('subscribers')
        return int(subscriber_count)
    except:
        return 0
