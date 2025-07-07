# https://zenquotes.io/api/random
# https://api-ninjas.com/api/quotes
# https://quoteslate.vercel.app/
# Создайте простое веб-приложение, которое будет запрашивать случайные цитаты с публичного API и отображать их на странице

from flask import Flask, render_template, request
import requests
import json
from config import API_KEY

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    try: # 1 quote_ninjas
        api_url = 'https://api.api-ninjas.com/v1/quotes'
        if request.method == 'GET':
            response = requests.get(api_url, headers={'X-Api-Key': API_KEY}, timeout=5)
            response.raise_for_status() # выбрасывает исключение в случае ошибки
            data = response.json()
            quote = data[0]["quote"]
            return  render_template("index.html", quote_ninjas=quote)
        elif request.method == 'POST':
            return  render_template("index.html", quote_ninjas='Испольщите GET для получения цитаты')
    except requests.exceptions.RequestException as e:
        return  render_template("index.html", quote_ninjas='Произошла ошибка при выполнении запроса: ' + str(e))

    try: # 2 zenquotes
        if request.method == 'GET':
            response = requests.get("https://zenquotes.io/api/random")
            quote = response.json()
            data = quote[0]["q"]
            return  render_template("index.html", quote_zenquotes=data)
        elif request.method == 'POST':
            return  render_template("index.html", quote_zenquotes='Испольщите GET для получения цитаты')
    except requests.exceptions.RequestException as e:
        return  render_template("index.html", quote_zenquotes='Произошла ошибка при выполнении запроса: ' + str(e))

    try: # 3 quoteslate
        url = "https://quoteslate.vercel.app/api/quotes/random"  # Подставьте реальный URL API
        if request.method == 'GET':
            response = requests.get(url)
            response.raise_for_status()  # Проверка ошибок
            quote = response.json()
            data2 = quote['quote']
            return  render_template("index.html", quote_quoteslate=data2)
        elif request.method == 'POST':
            return  render_template("index.html", quote_quoteslate='Испольщите GET для получения цитаты')
    except requests.exceptions.RequestException as e:
        return  render_template("index.html", quote_quoteslate='Произошла ошибка при выполнении запроса: ' + str(e))

if __name__ == '__main__':
    app.run(debug=True)