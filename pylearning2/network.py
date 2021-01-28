import requests
import socket
request = requests.get("http://www.google.com")

def check_connectivity():
    request = requests.get("http://www.google.com")
    status_code = request
    if request.status_code == [200]:
        print(True)

check_connectivity()