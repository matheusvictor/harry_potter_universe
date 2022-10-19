import requests as requests

from constants import Constants
from models.Spell import Spell
from models.Character import Character


class CharacterController:
    def __init__(self, data_source=None):
        self.__data_source = data_source
        self.__ravenclaw_characters = None
        self.__slytherin_characters = None
        self.__gryffindor_characters = None
        self.__hufflepuffe_characters = None

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

    def get_characters_by_house(self, mock=None, houses_name='gryffindor'):

        if type(mock) is str:
            raise NotImplementedError

        if mock is not None:
            request_to_json = mock
            print(type(request_to_json))
        else:
            print('Calling API...')
            request = requests.get(
                f'{Constants.base_url}/api/characters/house/{houses_name.lower()}')
            request_to_json = request.json()

        if houses_name.lower() == 'ravenclaw':
            self.__ravenclaw_characters = request_to_json
            return self.__ravenclaw_characters
        elif houses_name.lower() == 'gryffindor':
            self.__gryffindor_characters = request_to_json
            return self.__gryffindor_characters
        elif houses_name.lower() == 'slytherin':
            self.__slytherin_characters = request_to_json
            return self.__slytherin_characters
        elif houses_name.lower() == 'hufflepuffe':
            self.__hufflepuffe_characters = request_to_json
            return self.__hufflepuffe_characters
        else:
            raise NotImplementedError

    def get_character_by_name(self, name):
        for c in self.get_all_characters():
            if c.name == name:
                return c
            else:
                return None

    def get_spells_by_character_name(self, name) -> list[Spell]:
        characters = self.get_character_by_name(name)
        return characters.spells

    def learn_spell_by_character_name(self, spells_list, character_name, spell_name):
        character = self.get_character_by_name(character_name)

        if character is not None:
            for spell in spells_list:
                if spell.name == spell_name:
                    character.spells.add(spell)
                else:
                    print(f'{spell_name} not founded')

            for s in character.spells:
                print(s)
