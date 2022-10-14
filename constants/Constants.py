base_url = 'https://hp-api.onrender.com'

characters = '/api/characters'  # all characters
students = f'{characters}/students'  # characters who are Hogwarts students during the book series
staff = f'{characters}/staff'  # characters who are Hogwarts staff during the book series
characters_by_house = '/api/charactershouse/:house'  # characters in a certain house, e.g. /gryffindor
spells = '/api/spells'  # all spells
