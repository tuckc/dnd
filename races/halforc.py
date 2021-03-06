from race import Race

class Halforc(Race):
    def __init__(self):
        Race.__init__(self)
        self.strength = 2
        self.constitution = 1
        self.languages = ['Common', 'Orc']
        self.features = ['Darkvision', 'Relentless Endurance', 'Savage Attacks']
        self.proficiencies = ['Intimidation']
    def __str__(self):
        return super(Halforc,self).__str__()
        