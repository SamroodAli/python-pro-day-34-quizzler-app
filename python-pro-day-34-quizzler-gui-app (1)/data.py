"""Question data from Open Trivia Database"""
import requests

URL = "https://opentdb.com/api.php"
API_PARAMETERS = {
    "amount": 10,
    "type": "boolean",
}
RESPONSE = requests.get(url=URL, params=API_PARAMETERS)
RESPONSE.raise_for_status()
QUESTIONS_JSON = RESPONSE.json()
QUESTIONS_DATA = QUESTIONS_JSON["results"]
