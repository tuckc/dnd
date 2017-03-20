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
        self.proficiency = []
        self.cantrip = None
        if self.subrace is 'Forest Gnome':
            self.forest_gnome()
        if self.subrace is 'Rock Gnome':
            self.rock_gnome()

    def forest_gnome(self):
        self.dexterity = 1
        self.constitution = 0
        self.cantrip = 'Minor Illusion'
        if 'Speak with Small Beasts' not in self.other:
            self.other.append('Speak with Small Beasts')
        try:
            self.other.remove('Artificer\'s Lore')
            self.other.remove('Tinker')
        except ValueError:
            pass

    def rock_gnome(self):
        self.constitution = 1
        self.dexterity = 0
        self.cantrip = None
        if 'Tinker' not in self.other:
            self.other.append('Artificer\'s Lore')
            self.other.append('Tinker')
        try:
            self.other.remove('Speak with Small Beasts')
        except ValueError:
            pass
