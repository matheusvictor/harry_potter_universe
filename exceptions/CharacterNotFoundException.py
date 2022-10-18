class CharacterNotFoundException(Exception):
    def __init__(self, message='Character not founded!'):
        self.message = message

    def __str__(self):
        return self.message
