import requests
PARAMS = {
    "amount": "10",
    "type": "boolean"
}
question_data = requests.get("https://opentdb.com/api.php", params=PARAMS).json()["results"]
