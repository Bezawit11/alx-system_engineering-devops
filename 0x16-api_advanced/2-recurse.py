#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles
"""
import requests
import json

def recurse(subreddit, hot_list=[], after="")
    """ """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after)
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'}, allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return hot_list
    js = response.json()
    l = js.get("data")
    for i in l.get("children"):
        after = i.get("data").get("name")
        hot_list.append(i)
    recurse(subreddit, hot_list, after)
