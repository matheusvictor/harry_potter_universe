from controllers.CharacterController import *

if __name__ == '__main__':
    all_characters = get_all_characters()
    print(get_houses_name(all_characters))
    print(get_characters_by_house(all_characters, 'Ravenclaw'))
