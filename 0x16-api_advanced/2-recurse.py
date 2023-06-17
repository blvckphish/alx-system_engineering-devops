#!/usr/bin/python3
"""This file attempts to recursively
get all hot posts from the reddit api"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively get all posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
            'User-Agent': 'my_bot/1.0',
            }
    params = {'limit': '100'}
    if after:
        params['after'] = after

    response = requests.get(
            url,
            headers=headers, params=params, allow_redirects=False
            )
    if response.status_code != 200:
        return None

    domain = response.json().get('data').get('children')
    if not domain:
        return hot_list
    if hot_list:
        hot_list += [x.get('data').get('title') for x in domain]
    else:
        hot_list = [x.get('data').get('title') for x in domain]
    x = domain[-1]['kind'] + '_' + domain[-1]['data']['id']
    return recurse(subreddit, hot_list, after=x)
