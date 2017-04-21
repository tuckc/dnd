from race import Race

class Gnome(Race):
    def __init__(self, subrace):
        Race.__init__(self)
        self.intelligence = 2
        self.speed = 25
        self.languages = ['Common', 'Gnomish']
        self.features = ['Darkvision', 'Gnome Cunning']
        self.subrace = subrace
        if self.subrace == 'Forest Gnome':
            self._forest_gnome()
        if self.subrace == 'Rock Gnome':
            self._rock_gnome()

    def _forest_gnome(self):
        self.dexterity = 1
        self.cantrips.append('Minor Illusion')
        self.features.append('Speak with Small Beasts')

    def _rock_gnome(self):
        self.constitution = 1
        self.features.append('Artificer\'s Lore')
        self.features.append('Tinker')
    def __str__(self):
        return super(Gnome, self).__str__()
