#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api_url, verify=False).json()
    response = requests.get("{}users/{}".format(api_url, argv[1]))
    n = user.get('username')
    if n is not None:
        all_tasks = requests.get(
                "{}todos?userId={}".format(
                    api_url, argv[1])).json()

        with open("{}.csv".format(argv[1]), 'w') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for i in all_tasks:
                csvwriter.writerow("[i.get("userId"), n, i.get("completed"), i.get("title"))
