#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get("{}users/{}".format(api_url, sys.argv[0]))
    n = response.json().get("name")
    if n is not None:
        all_tasks = requests.get(
                "{}users/todos?userId={}".format(
                    url, user)).json()
        a = len(all_tasks)
        count = 0
        comp = []
        for i in all_tasks:
            if i["completed"] is True:
                count += 1
                comp.append(i)
        print("Employee {} is done with tasks({}/{}):".format(n, str(count)), a)
        for t in comp:
            print("\t {}".format(t["completed"]))
