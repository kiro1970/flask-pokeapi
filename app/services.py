from urllib import response
import requests as r
print('LOADING SERVICES')
pokemon = 'squirtle'
def getpokedata(pokemon):
    response = r.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    print(response.status_code)
    print(response)
    # pokedata = response
    # print(response.json())
    pokedata = response.json()
    return pokedata

class Pokemon:
    def __init__(self, pokedata):
        self.name = pokedata['name']
        self.attack = pokedata['stats']['1']['stat']['name']
        self.defense = pokedata['stats']['0']['stat']['name']
        
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
