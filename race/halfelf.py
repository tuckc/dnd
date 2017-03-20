class Halfelf(object):
    def __init__(self, abilities, language, proficiencies):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 1
        for ability in abilities:
            if ability is 'Strength':
                self.strength = 1
            elif ability is 'Dexterity':
                self.dexterity = 1
            elif ability is 'Constitution':
                self.constitution = 1
            elif ability is 'Intelligence':
                self.intelligence = 1
            else:
                self.wisdom = 1
        self.speed = 30
        self.languages = ['Common', 'Elvish', language]
        self.other = ['Darkvision', 'Fey Ancestry']
        self.proficiency = proficiencies
        self.cantrip = []
