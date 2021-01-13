"""Question data from Open Trivia Database"""
import requests

URL = "https://opentdb.com/api.php"
API_PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get(url=URL, params=API_PARAMETERS)
response.raise_for_status()
questions_json = response.json()
questions_data = questions_json["results"]
