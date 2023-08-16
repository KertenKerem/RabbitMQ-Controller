import json, requests, re

def get_queues(host, username, password, regex):
    url = f"http://{host}:15672/api/queues/"
    response = requests.get(url, auth=(username, password))
    queues = response.json()
    return [queue["name"] for queue in queues if queue["consumers"] == 0 and re.match(regex, queue['name'])]

host = "10.201.1.211"
username = "ynk"
password = "ynk"
regex = "^(?!_)([a-zA-Z0-9]+)$"

queues = get_queues(host, username, password, regex)
for queue in queues:
    print(queue)
