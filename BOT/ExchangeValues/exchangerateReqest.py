import requests
import asyncio
import json

async def get_values(value):
    url = "https://api.exchangerate.host/live?access_key=fa2db6be7aca816f1d323a106dcb493a&format=1"
    
    responce = requests.get(url)
    
    firstResult = responce.json()
    try:
        return f"Курс данной валюты:\n1 USD = {firstResult['quotes']['USD' + value]} {value}"
    except KeyError:
        return "Введена недоступная валюта!"