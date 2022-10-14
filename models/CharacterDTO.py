class CharacterDTO:
    def __init__(self, name, house, species, gender,
                 wizard, ancestry, date_of_birth, year_of_birth, image):
        self.name = name
        self.house = house
        self.species = species
        self.gender = gender
        self.wizard = wizard
        self.ancestry = ancestry
        self.dateOfBirth = date_of_birth
        self.yearOfBirth = year_of_birth
        self.image = image
        self.spells = []

    def to_dict(self):
        return self.__dict__

    def __str__(self):
        return f'{self.__dict__.values()}'.strip('dict_values()')
