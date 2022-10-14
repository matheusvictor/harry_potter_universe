class CharacterDTO:
    def __init__(self, name, house, species, gender,
                 wizard, ancestry, date_of_birth, year_of_birth, image):
        self.__name = name
        self.__house = house
        self.__species = species
        self.__gender = gender
        self.__wizard = wizard
        self.__ancestry = ancestry
        self.__date_of_birth = date_of_birth
        self.__year_of_birth = year_of_birth
        self.__image = image
        self.__spells = []

    @property
    def name(self):
        return self.__name

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, name):
        self.__house = name

    @property
    def species(self):
        return self.__species

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def wizard(self):
        return self.__wizard

    @property
    def ancestry(self):
        return self.__ancestry

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @property
    def year_of_birth(self):
        return self.__year_of_birth

    @property
    def image(self):
        return self.__image

    @property
    def spells(self):
        return self.__spells

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f'{self.__dict__.values()}'.strip('dict_values()')
