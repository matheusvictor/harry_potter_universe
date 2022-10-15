import requests as requests

from constants import Constants
from mocks import SpellsResponseMock
from models.CharacterDTO import CharacterDTO


def get_all_characters():
    request = requests.get(f'{Constants.base_url}{Constants.characters}')
    request_to_json = request.json()

    characters_list = list()
    for character in request_to_json:
        character = CharacterDTO(
            character['name'],
            character['house'],
            character['species'],
            character['gender'],
            character['wizard'],
            character['ancestry'],
            character['dateOfBirth'],
            character['yearOfBirth'],
            character['image']
        )
        if character.house == '':
            character.house = 'N/A'
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
    return characters_of_ravenclaw_house


def get_characters_of_hufflepuff_house(characters):
    characters_of_hufflepuff_house = set()
    for c in characters:
        if c.house == 'Hufflepuff':
            characters_of_hufflepuff_house.add(c)
    return characters_of_hufflepuff_house


def get_characters_of_slytherin_house(characters):
    characters_of_slytherin_house = set()
    for c in characters:
        if c.house == 'Slytherin':
            characters_of_slytherin_house.add(c)
    return characters_of_slytherin_house


def get_characters_of_gryffindor_house(characters):
    characters_of_gryffindor_house = set()
    for c in characters:
        if c.house == 'Gryffindor':
            characters_of_gryffindor_house.add(c)
    return characters_of_gryffindor_house


def get_characters_by_house(characters, houses_name):
    characters_by_house = set()
    for c in characters:
        if c.house == houses_name:
            characters_by_house.add(c)
    return characters_by_house


def get_spells_of_characters(characters):
    for c in characters:
        return c.spells


def get_spells_by_character_name(characters, name):
    for c in characters:
        if c.name == name:
            return c.spells


def get_character_by_name(characters, name):
    for c in characters:
        return c if c.name == name else None


def learn_spell_by_character_name(characters, name, spell_name):
    # spells = get_all_spells()
    spells = SpellsResponseMock.from_dto(SpellsResponseMock.get())  # mock list

    # if c.name == name:
    #     for s in spells:
    #         if s.name == spell_name:
    #             print(f'{c.name} learned {s.name} spell!')
