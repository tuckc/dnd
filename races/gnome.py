from race import Race

class Gnome(Race):
    def __init__(self, subrace):
        Race.__init__(self)
        self.intelligence = 2
        self.speed = 25
        self.languages = ['Common', 'Gnomish']
        self.features = ['Darkvision', 'Gnome Cunning']
        self.subrace = subrace
        if self.subrace is 'Forest Gnome':
            self.forest_gnome()
        if self.subrace is 'Rock Gnome':
            self.rock_gnome()

    def forest_gnome(self):
        self.dexterity = 1
        self.constitution = 0
        self.cantrip = 'Minor Illusion'
        if 'Speak with Small Beasts' not in self.features:
            self.features.append('Speak with Small Beasts')
        try:
            self.features.remove('Artificer\'s Lore')
            self.features.remove('Tinker')
        except ValueError:
            pass

    def rock_gnome(self):
        self.constitution = 1
        self.dexterity = 0
        self.cantrip = None
        if 'Tinker' not in self.features:
            self.features.append('Artificer\'s Lore')
            self.features.append('Tinker')
        try:
            self.features.remove('Speak with Small Beasts')
        except ValueError:
            pass
