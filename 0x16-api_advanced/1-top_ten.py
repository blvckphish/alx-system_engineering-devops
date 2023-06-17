#!/usr/bin/python3
"""This file gets the top ten hot posts
of a subreddit"""
import requests


def top_ten(subreddit):
    """Gets the top ten spots"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {'User-Agent': 'my_bot/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return
    domain = response.json().get('data').get('children')
    if domain:
        for i in range(10):
            print(domain[i].get('data').get('title'))
    else:
        print("None")
        return
