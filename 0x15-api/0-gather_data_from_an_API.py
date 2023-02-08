import requests
import sys
api_url = "https://jsonplaceholder.typicode.com/todos/" + str(sys.argv[1])
response = requests.get(api_url)
print(response.json())
