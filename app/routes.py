from urllib import response
from app import app
from flask import render_template
import requests
import json

@app.route('/')
def home():
    return render_template('index.html', title="PokeAPI Battler!")

@app.route('/howitworks')
def about():
    return render_template('howitworks.html', title="Learn how to battle!")

@app.route('/letsbattle')
def battle():
    req = requests.get('https://pokeapi.co/api/v2/pokemon/')
    print(req.status_code)
    data = json.loads(req.content)


    return render_template('letsbattle.html', title="Let's Battle!", data=data)


