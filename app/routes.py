print('LOADING ROUTES')
from urllib import response
from app import app
from flask import render_template
import requests
import json
print('LOADING ROUTES 2')
from app import services
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
def view():
    return render_template('letsbattle.html', title="Let's Battle!")

@app.route('/letsbattle', methods=['POST'])
def battle():
    req = requests.get('https://pokeapi.co/api/v2/pokemon/')
    print(req.status_code)
    data = json.loads(req.content)

    pokemon1 = services.getpokedata('Pikachu')
    pokemon1 = services.Pokemon(pokemon1)
    pokemon2 = services.getpokedata('Mewtwo')
    pokemon2 = services.Pokemon(pokemon2)
    outcome1 = pokemon1.attack - pokemon2.defense
    outcome2 = pokemon2.attack - pokemon1.defense
    if outcome1 > outcome2:
        winner = pokemon1
    elif outcome2 > outcome1:
        winner = pokemon2
    elif pokemon1.hp > pokemon2.hp:
        winner = pokemon1
    else:
         winner = pokemon2
    
    
# DO BATTLE MATH - RETURN WINNER

    return render_template('letsbattle.html', title="Let's Battle!", winner=winner)

