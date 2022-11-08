import requests
from pprint import pprint
from random import randint
import json


def req(url):
    data = requests.get(url).json()
    return data


def character():
    character = (f'Имя персонажа - {characters["results"][randint(0,19)]["name"]}\n'
                 f'Состояние - {characters["results"][randint(0,19)]["status"]}\n'
                 f'Вид - {characters["results"][randint(0,19)]["species"]}\n'
                 f'Пол - {characters["results"][randint(0,19)]["gender"]}\n'
                 f'Родина - {characters["results"][randint(0,19)]["origin"]["name"]}'
                 )
    return character


r = req('https://rickandmortyapi.com/api')
characters = req(r['characters'])


print(character())
