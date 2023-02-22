#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    dictionary = {}
    for a in range(1, len(response.json()) + 1):
        n = response.json()[a - 1]['username']
        all_tasks = requests.get(
            "{}todos?userId={}".format(
                api_url, a)).json()
        j = []
        for i in all_tasks:
            u = i['userId']
            k = {'username': n, 'title': i['title'], 'completed': i['completed']}
            j.append(k)
        dictionary.update({a: j})
        j = []
    filename = "todo_all_employees.json"
    with open(filename, 'w', newline='') as jsonfile:
        json.dump(dictionary, jsonfile)
