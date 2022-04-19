print('LOADING ROUTES')
from urllib import response
from app import app
from flask import render_template
import requests
import json
print('LOADING ROUTES 2')
#import app.services
#from services import Pokemon
#from services import getpokedata
print('LOADING ROUTES 3')

@app.route('/')
def home():
    print('IN HOME RUTE!!!!!!')
    return render_template('index.html', title="PokeAPI BattlerXXX!")

@app.route('/howitworks')
def about():
    return render_template('howitworks.html', title="Learn how to battle!")

@app.route('/letsbattle')
def battle():
    req = requests.get('https://pokeapi.co/api/v2/pokemon/')
    print(req.status_code)
    data = json.loads(req.content)
    pokemon1 = app.services.getpokedata('Pikachu')
    pokemon1 = app.services.Pokemon(pokemon1)
    pokemon2 = app.services.getpokedata('Mewtwo')
    pokemon2 = app.services.Pokemon(pokemon2)


    return render_template('letsbattle.html', title="Let's Battle!", data=data, pokemon1=pokemon1, pokemon2=pokemon2)


