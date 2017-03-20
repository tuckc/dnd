class Gnome(object):
    def __init__(self, subrace):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 2
        self.wisdom = 0
        self.charisma = 0
        self.speed = 25
        self.languages = ['Common', 'Gnomish']
        self.other = ['Darkvision', 'Gnome Cunning']
        self.subrace = subrace
        if self.subrace is 'Forest Gnome':
            forest_gnome(self)
        if self.subrace is 'Rock Gnome':
            rock_gnome(self)
        self.proficiency = []
        self.cantrip = []

def forest_gnome(gnome):
    gnome.dexterity = 1
    gnome.constitution = 0
    gnome.other.append('Speak with Small Beasts')
    try:
        gnome.other.remove('Artificer\'s Lore')
        gnome.other.remove('Tinker')
    except ValueError:
        pass

def rock_gnome(gnome):
    gnome.constitution = 1
    gnome.dexterity = 0
    gnome.other.append('Artificer\'s Lore')
    gnome.other.append('Tinker')
    try:
        gnome.other.remove('Speak with Small Beasts')
    except ValueError:
        pass
