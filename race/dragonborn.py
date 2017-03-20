class Dragonborn(object):
    def __init__(self, ancestry):
        self.strength = 2
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 1
        self.speed = 30
        self.languages = ['Common', 'Draconic']
        self.other = [
            'Draconic Ancestry: ' + ancestry,
            'Breath Weapon',
            'Damage Resistance(' + ancestry + ')'
        ]
        self.proficiency = []
        self.cantrip = None
