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
        if self.subrace is 'Hill Dwarf':
            hill_dwarf(self)
        if self.subrace is 'Mountain Dwarf':
            mountain_dwarf(self)

def hill_dwarf(dwarf):
    dwarf.wisdom = 1
    dwarf.strength = 0
    try:
        dwarf.other.remove('Light Armor')
        dwarf.other.remove('Medium Armor')
    except ValueError:
        pass

def mountain_dwarf(dwarf):
    dwarf.strength = 2
    dwarf.wisdom = 0
    dwarf.other.extend(['Light Armor', 'Medium Armor'])
