from __future__ import print_function
from race import Race

class Elf(Race):
    def __init__(self, subrace, cantrip=None, language=None):
        Race.__init__(self)
        self.dexterity = 2
        self.languages = ['Common', 'Elvish']
        self.features = ['Darkvision', 'Fey Ancestry', 'Trance']
        self.subrace = subrace
        self.proficiencies = ['Perception']
        if self.subrace == 'High Elf':
            self._high_elf(cantrip, language)
        if self.subrace == 'Wood Elf':
            self._wood_elf()
        if self.subrace == 'Dark Elf (Drow)':
            self._dark_elf()

    def _high_elf(self, cantrip, language):
        self.intelligence = 1
        self.speed = 30
        self.cantrips.append(cantrip)
        self.languages.append(language)
        self.other.extend(['Longsword', 'Shortsword', 'Shortbow', 'Longbow'])

    def _wood_elf(self):
        self.wisdom = 1
        self.speed = 35
        self.cantrips = []
        self.features.append('Mask of the Wild')
        self.other.extend(['Longsword', 'Shortsword', 'Shortbow', 'Longbow'])

    def _dark_elf(self):
        self.charisma = 1
        self.speed = 30
        self.cantrips.append('Dancing Light')
        self.other.extend(['Rapier', 'Shortsword', 'Hand Crossbow'])
        self.features[self.features.index('Darkvision')] = 'Superior Darkvision'

    def __str__(self):
        return super(Elf, self).__str__()