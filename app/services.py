from urllib import response
import requests as r
print('LOADING SERVICES')
pokemon = 'squirtle'
def getpokedata(pokemon):
    pokemon = pokemon.lower()
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    print(url)
    response = r.get(url)
    print(response.status_code)
    print(response)
    # pokedata = response
    # print(response.json())
    pokedata = response.json()
    return pokedata

class Pokemon:
    def __init__(self, pokedata):
        print('CLASS INIT')
        self.sprite = pokedata['sprites']['front_default']
        self.name = pokedata['name']
        self.hp = pokedata['stats'][0]['base_stat']
        self.attack = pokedata['stats'][1]['base_stat']
        self.defense = pokedata['stats'][2]['base_stat']
        print(f'Attack {self.attack}')
        
    def printInfo(self):
        print(f'Name: {self.name.capitalize()}')
        for t in self.types:
            n = t['type']['name']
            print("Type: " + n)
        
        for a in self.abilities:
            n = a['ability']['name']
            print("Ability: " + n)
            
#print(Pokemon(pokedata))
#e = Pokemon(pokedata)
#print(f'Here is name from a Pokemon object: {e.name}')
