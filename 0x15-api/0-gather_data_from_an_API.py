#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get("{}users/{}".format(api_url, argv[1]))
    n = response.json().get("name")
    if n is not None:
        all_tasks = requests.get(
                "{}todos?userId={}".format(
                    api_url, argv[1])).json()
        a = len(all_tasks)
        count = 0
        comp = []
        for i in all_tasks:
            if i["completed"] is True:
                count += 1
                comp.append(i)
        print("Employee {} is done with tasks({}/{}):".format(n, count, a))
        for t in comp:
            print("\t {}".format(t["completed"]))
