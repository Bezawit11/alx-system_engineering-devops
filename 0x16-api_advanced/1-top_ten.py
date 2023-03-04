#!/usr/bin/python3
"""
returns top ten hot posts
"""
import json
import requests


def top_ten(subreddit):
    """ """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'}, allow_redirects=False)
    if response.status_code == 200:
        js = response.json()
        l = js.get("data")
        for i in l.get("children"):
            try:
                print(i.get("data").get("title"))
            except:
                print(i.get("data").get("title").encode())
    else:
        print("None")
