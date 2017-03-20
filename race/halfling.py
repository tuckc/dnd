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
        if self.subrace is 'Lightfoot':
            lightfoot(self)
        if self.subrace is 'Stout':
            stout(self)

def lightfoot(halfling):
    halfling.charisma = 1
    halfling.constitution = 0
    halfling.other.append('Naturally Stealthy')
    try:
        halfling.other.remove('Stout Resillience')
    except ValueError:
        pass

def stout(halfling):
    halfling.constitution = 1
    halfling.charisma = 0
    halfling.other.append('Stout Resillience')
    try:
        halfling.other.remove('Naturally Stealthy')
    except ValueError:
        pass
