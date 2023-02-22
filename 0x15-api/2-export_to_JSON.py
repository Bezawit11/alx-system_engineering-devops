#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get("https://jsonplaceholder.typicode.com/users?id={}".
			format(argv[1]))
    n = response.json()[0]['username']
    filename = "{}.json".format(argv[1])
    all_tasks = requests.get(
            "{}todos?userId={}".format(
                api_url, argv[1])).json()
    j = []
    for i in all_tasks:
        a = i['userId']
        k = {'task': i['title'], 'completed': i['completed'], 'username': n}
        j.append(k)
    dictionary = {a: j}
    with open(filename, 'w', newline='') as jsonfile:
        json.dump(dictionary, jsonfile)
