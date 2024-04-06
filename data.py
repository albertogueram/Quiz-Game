import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
if response.status_code != 200:
    raise Exception("Open Trivia Database API Issue")
else:
    question_data = response.json()["results"]
