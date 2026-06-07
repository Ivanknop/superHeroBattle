import requests,json
import handler_db


def superHero(especification):
        url = 'https://superheroapi.com/api.php/10229065685292237/'+especification+'/powerstats'
        resp = requests.get(url)
        if resp.status_code == 200:
            content = resp.content
            res_dict = json.loads(content.decode('utf-8'))
            return res_dict
        else:
            return 'Error'

#print(superHero('batman')['results'][1]['powerstats'])

lista_personajes = []
for i in range(1,5):
    lista_personajes.append(superHero(str(i)))

lista_personajes.append(superHero(str(729)))

for p in lista_personajes:
    print(p)



print(handler_db.find_hero('batman'))