#!/usr/bin/python3
"""Gather data from an API"""
import csv
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
        rows = [[]]
        r = []
        for dict in all_tasks:
            for k,v in dict.items():
                if k != "id":
                    r.append(v)
                if k == "userId":
                    filename = "{}.csv".format(v)
                    r.append(n)
            #h = r[3]
            #m = r[2]
            #r[2] = h
            #r[3] = m
            rows.append(r)
            r = []
        
        #"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            csvwriter.writerows(rows)

