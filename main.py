from controllers.CharacterController import *
from exceptions.CharacterNotFoundException import CharacterNotFoundException

if __name__ == '__main__':
    all_characters = get_all_characters()

    # houses_name = get_character_houses_name(all_characters)
    # for name in houses_name:
    #     print(name)
    #
    # print('*' * 60)
    # ravenclaw = get_characters_of_ravenclaw_house(all_characters)
    # for character in ravenclaw:
    #     print(character.name)

    # get_spells_by_character_name(all_characters, 'Luna Lovegood')
    # learn_spell_by_character_name(all_characters, 'Luna Lovegood', 'Aberto')
    # get_spells_by_character_name(all_characters, 'Luna Lovegood')
    # print(CharacterByHouseResponseMock.get())

    if get_character_by_name(all_characters, 'Jack') is None:
        raise CharacterNotFoundException('Char not found!')

    print(get_character_by_name(all_characters, 'Luna Lovegood'))
