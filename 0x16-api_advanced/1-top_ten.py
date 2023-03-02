#!/usr/bin/python3
"""
returns top ten hot posts
"""
import requests
import json


def top_ten(subreddit):
    """ """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'}, allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        js = response.json()
        titles_ = js.get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
