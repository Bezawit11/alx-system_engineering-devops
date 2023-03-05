#!/usr/bin/python3
"""
returns a list containing the titles of all hot articles
"""
import json
import requests

dict = {}
def count_words(subreddit, word_list, after=None):
    """ recursive function that queries the Reddit API and returns a
    list containing the titles of all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?'.format(subreddit)
    parameter = {'after': after}
    response = requests.get(url, headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Jazzlike_Day2550)'}, params=parameter, allow_redirects=False)
    if response.status_code != 200:
        return None
    js = response.json()
    l = js.get("data")
    after = l.get("after")
    for j in word_list:
        global dict[j] = 0
    if after is not None:
        count_words(subreddit, word_list, after):
    for i in l.get("children"):
        title = i.get("data").get("title")
        for k in my_list:
            if k in title:
                global dict[k] = dict[j] + 1
    print(dict)
    
