mnbvcxz1
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
        filename = "{}.csv".format(argv[1])
        all_tasks = requests.get(
                "{}todos?userId={}".format(
                    api_url, argv[1])).json()
        
        #"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for i in all_tasks:
                csvwriter.writerow([int(argv[1]), i.get('userId'), i.get('completed'), i.get('title')])
