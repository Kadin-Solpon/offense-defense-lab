import requests

url = ''

with open('./defensive/defend/webhookurl.txt') as file:
    url = file.readline()

def send_message(message):
    requests.post(url, json= {'text': message})