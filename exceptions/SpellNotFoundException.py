class SpellNotFoundException:
    def __init__(self, message='Spell not founded!'):
        self.message = message

    def __str__(self):
        return self.message
