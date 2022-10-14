import requests as requests

from constants import Constants
from models.CharacterDTO import CharacterDTO


def get_all_characters():
    request = requests.get(f'{Constants.base_url}{Constants.characters}')
    request_to_json = request.json()
    characters_list = list()

    for character_raw in request_to_json:
        character = CharacterDTO(
            character_raw['name'],
            character_raw['house'],
            character_raw['species'],
            character_raw['gender'],
            character_raw['wizard'],
            character_raw['ancestry'],
            character_raw['dateOfBirth'],
            character_raw['yearOfBirth'],
            character_raw['image']
        )
        characters_list.append(character)

    return characters_list


def get_houses_name(characters):
    houses_name = set()
    for c in characters:
        houses_name.add(c.house)
    return houses_name


def get_characters_of_ravenclaw_house(characters):
    characters_of_ravenclaw_house = set()
    for c in characters:
        if c.house == 'Ravenclaw':
            characters_of_ravenclaw_house.add(c)
            print(c.name)
    return characters_of_ravenclaw_house


def get_characters_of_hufflepuff_house(characters):
    characters_of_hufflepuff_house = set()
    for c in characters:
        if c.house == 'Hufflepuff':
            characters_of_hufflepuff_house.add(c)
            print(c.name)
    return characters_of_hufflepuff_house


def get_characters_of_slytherin_house(characters):
    characters_of_slytherin_house = set()
    for c in characters:
        if c.house == 'Slytherin':
            characters_of_slytherin_house.add(c)
            print(c.name)
    return characters_of_slytherin_house


def get_characters_of_gryffindor_house(characters):
    characters_of_gryffindor_house = set()
    for c in characters:
        if c.house == 'Gryffindor':
            characters_of_gryffindor_house.add(c)
            print(c.name)
    return characters_of_gryffindor_house


def get_characters_by_house(characters, houses_name):
    characters_by_house = set()
    for c in characters:
        if c.house == houses_name:
            characters_by_house.add(c)
            print(c.name)
    return characters_by_house
