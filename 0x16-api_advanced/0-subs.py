#!/usr/bin/python3
"""This file queries the reddit api for a
given subreddit and returns the number of
subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Gets the number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    x = response.json()
    if x:
        data = x.get('data')
        if data:
            ans = data.get('subscribers')
            if ans:
                return ans
    return 0
