from controllers.CharacterController import *
from controllers.SpellController import *
from mocks.CharactersByHouseResponseMock import CharactersByHouseResponseMock
from mocks.CharactersResponseMock import CharactersResponseMock
from mocks.SpellsResponseMock import SpellsResponseMock

if __name__ == '__main__':
    characters_mock = CharactersResponseMock()
    characters_controller = CharacterController(characters_mock)

    spells_mock = SpellsResponseMock()
    spells_controller = SpellController(spells_mock)

    r = CharactersByHouseResponseMock.get('Ravenclaw')
    print(characters_controller.get_characters_by_house('a'))

    # print(spells_controller.get_spell_by_name('Alakazan'))
    # print(spells_controller.get_spell_by_name('Aberto'))
    #
    # print(characters_controller.learn_spell_by_character_name(spells_controller.get_all_spells(), 'Harry Potter', 'B'))

    # spells_mock = SpellsResponseMock()
    # print(characters_controller.get_spells_by_character_name('Harry Potter'))
    # characters_controller.learn_spell_by_character_name('H', 'Aberto')
    # characters_controller.learn_spell_by_character_name('Harry Potter', 'A')

    # if get_character_by_name(all_characters, 'Jack') is None:
    #     raise CharacterNotFoundException('Char not found!')
    #
    # print(get_character_by_name(all_characters, 'Luna Lovegood'))
