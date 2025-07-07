# https://zenquotes.io/api/random
# https://api-ninjas.com/api/quotes
# https://quoteslate.vercel.app/
# Создайте простое веб-приложение, которое будет запрашивать случайные цитаты с публичного API и отображать их на странице

from flask import Flask, render_template, request
import requests
from config import API_KEY
import json

# 1.
print()
api_url = 'https://api.api-ninjas.com/v1/quotes'
words = []
# if request.method == 'POST':
    # word = request.form['word']
response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    data = response.text
    data = json.loads(data)
    quote_value = data[0]["quote"]
    print(quote_value)
else:
    print("Error:", response.status_code, response.text)

print()

# 2.
response = requests.get("https://zenquotes.io/api/random")
quote = response.json()
print(quote[0]["q"])

# 3.
print()
url = "https://quoteslate.vercel.app/api/quotes/random"  # Подставьте реальный URL API

try:
    response = requests.get(url)
    response.raise_for_status()  # Проверка ошибок
    quote = response.json()
    print(f"Цитата: {quote['quote']}")
except Exception as e:
    print(f"Ошибка: {e}")