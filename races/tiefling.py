from race import Race

class Tiefling(Race):
    def __init__(self):
        Race.__init__(self)
        self.intelligence = 1
        self.charisma = 2
        self.languages = ['Common', 'Infernal']
        self.features = ['Darkvision', 'Hellish Resistance', 'Infernal Legacy']
        self.cantrips = ['Thaumaturgy']
    def __str__(self):
        return super.__str__(self)
