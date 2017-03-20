class Halfling(object):
    def __init__(self, subrace):
        self.strength = 0
        self.dexterity = 2
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.speed = 25
        self.languages = ['Common', 'Halfling']
        self.other = ['Lucky', 'Brave', 'Halfling Nimbleness']
        self.subrace = subrace
        self.proficiency = []
        self.cantrip = None
        if self.subrace is 'Lightfoot':
            self.lightfoot()
        if self.subrace is 'Stout':
            self.stout()

    def lightfoot(self):
        self.charisma = 1
        self.constitution = 0
        if 'Naturally Stealthy' not in self.other:
            self.other.append('Naturally Stealthy')
        try:
            self.other.remove('Stout Resillience')
        except ValueError:
            pass

    def stout(self):
        self.constitution = 1
        self.charisma = 0
        if 'Stout Resillience' not in self.other:
            self.other.append('Stout Resillience')
        try:
            self.other.remove('Naturally Stealthy')
        except ValueError:
            pass
