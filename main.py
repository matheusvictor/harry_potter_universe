from controllers.CharacterController import *
from mocks import CharacterByHouseResponseMock

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
    learn_spell_by_character_name(all_characters, 'Luna Lovegood')
    # get_spells_by_character_name(all_characters, 'Luna Lovegood')

    print(CharacterByHouseResponseMock.get())
