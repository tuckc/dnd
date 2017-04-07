from race import Race

class Halfling(Race):
    def __init__(self, subrace):
        Race.__init__(self)
        self.dexterity = 2
        self.speed = 25
        self.languages = ['Common', 'Halfling']
        self.features = ['Lucky', 'Brave', 'Halfling Nimbleness']
        self.subrace = subrace
        if self.subrace is 'Lightfoot Halfling':
            self._lightfoot()
        if self.subrace is 'Stout Halfling':
            self._stout()

    def _lightfoot(self):
        self.charisma = 1
        self.features.append('Naturally Stealthy')

    def _stout(self):
        self.constitution = 1
        self.features.append('Stout Resillience')
        