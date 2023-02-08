#!/usr/bin/python3
import requests
import sys
if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    response = requests.get(api_url)
    print(response.json())
