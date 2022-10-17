import requests as requests

from constants import Constants
from models.Spell import Spell


class SpellController:
    def __init__(self, data_source=None):
        self.__data_source = data_source

    def get_all_spells(self):
        if self.__data_source:
            request_to_json = self.__data_source.get()
        else:
            request = requests.get(f'{Constants.base_url}{Constants.spells}')
            request_to_json = request.json()

        spells_list = list()
        for spell in request_to_json:
            spell = Spell(
                spell['name'],
                spell['description']
            )
            spells_list.append(spell)
        return spells_list

    def get_spell_by_name(self, name):
        for spell in self.get_all_spells():
            if spell.name == name:
                print(self.__data_source)
                return spell
