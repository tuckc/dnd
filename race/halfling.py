from race import Race

class Halfling(Race):
    def __init__(self, subrace):
        Race.__init__()
        self.dexterity = 2
        self.speed = 25
        self.languages = ['Common', 'Halfling']
        self.features = ['Lucky', 'Brave', 'Halfling Nimbleness']
        self.subrace = subrace
        if self.subrace is 'Lightfoot':
            self.lightfoot()
        if self.subrace is 'Stout':
            self.stout()

    def lightfoot(self):
        self.charisma = 1
        self.constitution = 0
        if 'Naturally Stealthy' not in self.features:
            self.features.append('Naturally Stealthy')
        try:
            self.features.remove('Stout Resillience')
        except ValueError:
            pass

    def stout(self):
        self.constitution = 1
        self.charisma = 0
        if 'Stout Resillience' not in self.features:
            self.features.append('Stout Resillience')
        try:
            self.features.remove('Naturally Stealthy')
        except ValueError:
            pass
