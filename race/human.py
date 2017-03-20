class Human(object):
    def __init__(self, language):
        self.strength = 1
        self.dexterity = 1
        self.constitution = 1
        self.intelligence = 1
        self.wisdom = 1
        self.charisma = 1
        self.speed = 30
        self.languages = ['Common', language]
        self.other = []
        self.proficiency = []
        self.cantrip = None
        