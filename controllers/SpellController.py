import requests as requests

from constants import Constants
from models.SpellDTO import SpellDTO


def get_all_spells() -> list:
    request = requests.get(f'{Constants.base_url}{Constants.spells}')
    request_to_json = request.json()

    spells_list = list()
    for spell in request_to_json:
        spell = SpellDTO(
            spell['name'],
            spell['description']
        )
        spells_list.append(spell)
    return spells_list
