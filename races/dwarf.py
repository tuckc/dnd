from race import Race

class Dwarf(Race):
    def __init__(self, subrace, tool):
        Race.__init__(self)
        self.constitution = 2
        self.speed = 25
        self.languages = ['Common', 'Dwarvish']
        self.features = [
            'Darkvision',
            'Dwarven Resillience',
            'Stone Cunning'
        ]
        self.other = [
            'Battleaxe',
            'Handaxe',
            'Throwing Hammer',
            'Warhammer',
            tool
        ]
        self.subrace = subrace
        if self.subrace is 'Hill Dwarf':
            self.hill_dwarf()
        if self.subrace is 'Mountain Dwarf':
            self.mountain_dwarf()

    def hill_dwarf(self):
        self.wisdom = 1
        self.strength = 0
        if 'Dwarven Toughness' not in self.features:
            self.features.append('Dwarven Toughness')
        try:
            self.other.remove('Light Armor')
            self.other.remove('Medium Armor')
        except ValueError:
            pass

    def mountain_dwarf(self):
        self.strength = 2
        self.wisdom = 0
        if 'Light Armor' not in self.other:
            self.other.extend(['Light Armor', 'Medium Armor'])
        try:
            self.features.remove('Dwarven Toughness')
        except ValueError:
            pass
