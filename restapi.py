import requests

response = requests.get('http://localhost:8080/stats/switches')
print(response.reason)
print("hiii")