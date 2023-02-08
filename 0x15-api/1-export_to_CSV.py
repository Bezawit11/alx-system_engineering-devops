#!/usr/bin/python3
"""Gather data from an API"""
import csv
import requests
from sys import argv
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get("https://jsonplaceholder.typicode.com/users?id={}".format(argv[1]))
    n = response.json().get('username')
    filename = "{}.csv".format(argv[1])
    all_tasks = requests.get(
            "{}todos?userId={}".format(
                api_url, argv[1])).json()
    #"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in all_tasks:
            csvwriter.writerow([str(i.get('userId')), n,
                                str(i.get('completed')), i.get('title')])
            
