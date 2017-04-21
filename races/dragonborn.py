from race import Race

class Dragonborn(Race):
    def __init__(self, ancestry):
        Race.__init__(self)
        self.strength = 2
        self.charisma = 1
        self.languages = ['Common', 'Draconic']
        self.features = [
            'Draconic Ancestry: ' + ancestry,
            'Breath Weapon',
            'Damage Resistance(' + ancestry + ')'
        ]
    def __str__(self):
        return super.__str__(self)
