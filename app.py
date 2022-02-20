import requests
import os
from dotenv import load_dotenv

load_dotenv()

trello_apiKey = os.getenv("APIKEY_TRELLO")
trello_token = os.getenv("TOKEN_TRELLO")
tarjeta = input("Título de la tarjeta: ")

url = f"https://api.trello.com/1/cards?idList=61a3c12411b6200ceae1b532&key={trello_apiKey}&token={trello_token}&name={tarjeta}"

payload = {}
headers = {
    'Cookie': 'dsc=9f69975cb82d0219525db6aefd8fee2a73312cd4aa98c700fb6d24f66e6a8c73'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)