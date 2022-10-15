import requests as requests

from constants import Constants
from models.Spell import Spell
from models.Character import Character


class CharacterController:
    def __init__(self, data_source=None):
        self.__data_source = data_source

    def get_all_characters(self):
        if self.__data_source:
            request_to_json = self.__data_source.get()
        else:
            request = requests.get(f'{Constants.base_url}{Constants.characters}')
            request_to_json = request.json()

        characters_list = list()
        for character in request_to_json:
            character = Character(
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

    def get_houses_name(self):
        houses_name = set()
        for c in self.get_all_characters():
            houses_name.add(c.house)
        return houses_name

    def get_characters_of_ravenclaw_house(self):
        characters_of_ravenclaw_house = set()
        for c in self.get_all_characters():
            if c.house == 'Ravenclaw':
                characters_of_ravenclaw_house.add(c)
        return characters_of_ravenclaw_house

    def get_characters_of_hufflepuff_house(self):
        characters_of_hufflepuff_house = set()
        for c in self.get_all_characters():
            if c.house == 'Hufflepuff':
                characters_of_hufflepuff_house.add(c)
        return characters_of_hufflepuff_house

    def get_characters_of_slytherin_house(self):
        characters_of_slytherin_house = set()
        for c in self.get_all_characters():
            if c.house == 'Slytherin':
                characters_of_slytherin_house.add(c)
        return characters_of_slytherin_house

    def get_characters_of_gryffindor_house(self):
        characters_of_gryffindor_house = set()
        for c in self.get_all_characters():
            if c.house == 'Gryffindor':
                characters_of_gryffindor_house.add(c)
        return characters_of_gryffindor_house

    def get_characters_by_house(self, houses_name):
        characters_by_house = set()
        for c in self.get_all_characters():
            if c.house == houses_name:
                characters_by_house.add(c)
        return characters_by_house

    def get_spells_by_character_name(self, name) -> list[Spell]:
        characters = self.get_character_by_name(name)
        return characters.spells

    def get_character_by_name(self, name):
        for c in self.get_all_characters():
            if c.name == name:
                return c
            else:
                return None

    def learn_spell_by_character_name(self, characters, name, spell_name):
        raise NotImplementedError
