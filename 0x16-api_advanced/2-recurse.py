#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles
"""
import requests
import json

def recurse(subreddit, hot_list=[], after=None):
    """ """
    url = 'https://www.reddit.com/r/{}/hot.json?'.format(subreddit)
    parameter = {'after': after}
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'}, params=parameter, allow_redirects=False)
    if response.status_code != 200:
        return None
    js = response.json()
    l = js.get("data")
    after = l.get("after")
    for i in l.get("children"):
        title = i.get("data").get("title")
        hot_list.append(title)
    if after is not None:
        recurse(subreddit, hot_list, after)
    else:    
        return hot_list
