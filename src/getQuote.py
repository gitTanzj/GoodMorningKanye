import requests
import json

class Quote():
    def getData():
        response_API = requests.get("https://api.kanye.rest/")
        response = json.loads(response_API.text)
        return response['quote']





    
        