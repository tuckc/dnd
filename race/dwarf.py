class Dwarf(object):
    def __init__(self, subrace, tool):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 2
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.speed = 25
        self.languages = ['Common', 'Dwarvish']
        self.other = [
            'Darkvision',
            'Dwarven Resillience',
            'Battleaxe',
            'Handaxe',
            'Throwing Hammer',
            'Warhammer',
            tool,
            'Stone Cunning'
        ]
        self.subrace = subrace
        self.proficiency = []
        self.cantrip = None
        if self.subrace is 'Hill Dwarf':
            self.hill_dwarf()
        if self.subrace is 'Mountain Dwarf':
            self.mountain_dwarf()

    def hill_dwarf(self):
        self.wisdom = 1
        self.strength = 0
        if 'Dwarven Toughness' not in self.other:
            self.other.append('Dwarven Toughness')
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
            self.other.remove('Dwarven Toughness')
        except ValueError:
            pass
