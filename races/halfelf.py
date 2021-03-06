from race import Race

class Halfelf(Race):
    def __init__(self, language, abilities=None):    #add proficiencies later
        Race.__init__(self)
        self.charisma = 1
        if abilities:
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
        self.languages = ['Common', 'Elvish', language]
        self.features = ['Darkvision', 'Fey Ancestry']
        self.proficiencies = []

    def setProficiencies(self, p):
        self.proficiencies.extend(p)
        
    def __str__(self):
        return super(Halfelf, self).__str__()
