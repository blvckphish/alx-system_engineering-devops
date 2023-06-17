#!/usr/bin/python3
"""This file attempts to recursively
get all hot posts from the reddit api"""
import re
import requests


def match(string, text):
    """Uses regex to find all occurences of a string"""
    pattern = r"\b{}\b".format(string)
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)


def _print(curr):
    """Prints out the dictionary"""
    for k, v in sorted(curr.items(), key=lambda x: (-x[1], x[0])):
        if v != 0:
            print("{}: {}".format(k, v))


def count_words(subreddit, word_list=[], hot_dict={}, after=None):
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
    if not hot_dict:
        word_list = set([x.lower() for x in word_list])
        hot_dict = {x: 0 for x in word_list}
    if response.status_code != 200:
        _print(hot_dict)
        return

    domain = response.json().get('data').get('children')
    if not domain:
        _print(hot_dict)
        return
    hot_list = [x.get('data').get('title') for x in domain]
    for k, v in hot_dict.items():
        for title in hot_list:
            hot_dict[k] += match(k, title)
    x = domain[-1]['kind'] + '_' + domain[-1]['data']['id']
    return count_words(subreddit, word_list, hot_dict, after=x)
