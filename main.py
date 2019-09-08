import json
import requests
from flask import jsonify

def getIngressos():
    api_url = 'http://localhost:5000/ingressos'
    response = requests.get(api_url)

    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print("Não deu certo")

def getOneIngresso(id):
    api_url = 'http://localhost:5000/ingressos/' + str(id)
    response = requests.get(api_url)

    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print("Não deu certo")
        
def insertIngresso(ingresso):
    api_url = 'http://localhost:5000/ingressos'
    response = requests.post(api_url, json=ingresso)
    
    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print("Não deu certo")

def updateIngresso(ingresso):
    api_url = 'http://localhost:5000/ingressos'
    response = requests.put(api_url, json=ingresso)
    
    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print("Não deu certo")

def deleteIngresso(id):
    api_url = 'http://localhost:5000/ingressos/' + str(id)
    response = requests.delete(api_url)
    
    if response.status_code == 200:
        print(json.loads(response.content.decode('utf-8')))
    else:
        print("Não deu certo")

getIngressos()