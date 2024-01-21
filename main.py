import requests
# https://ngl.link/api/submit

username = "cottonfarmer112"
question = "cottonfarmer112"

data = {
    "username": username,
    "question": question,
    "deviceId": "e6baa765-afad-4885-a06f-13b5d54d7ce7"
}


try:
    response = requests.post("https://ngl.link/api/submit", data=data)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(e)