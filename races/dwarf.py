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
        if self.subrace == 'Hill Dwarf':
            self._hill_dwarf()
        if self.subrace == 'Mountain Dwarf':
            self._mountain_dwarf()

    def _hill_dwarf(self):
        self.wisdom = 1
        self.features.append('Dwarven Toughness')

    def _mountain_dwarf(self):
        self.strength = 2
        self.other.extend(['Light Armor', 'Medium Armor'])
        