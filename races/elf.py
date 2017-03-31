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
        if self.subrace is 'High Elf':
            self.high_elf(cantrip, language)
        if self.subrace is 'Wood Elf':
            self.wood_elf()
        if self.subrace is 'Dark Elf (Drow)':
            self.dark_elf()

    def high_elf(self, cantrip, language):
        self.intelligence = 1
        self.wisdom = 0
        self.charisma = 0
        self.speed = 30
        self.cantrip = cantrip
        self._high_elf_check()
        self.languages.append(language)

    def wood_elf(self):
        self.wisdom = 1
        self.intelligence = 0
        self.charisma = 0
        self.speed = 35
        self.cantrip = None
        self._wood_elf_check()

    def dark_elf(self):
        self.charisma = 1
        self.intelligence = 0
        self.wisdom = 0
        self.speed = 30
        self.cantrip = 'Dancing Light'
        self._dark_elf_check()

    def _high_elf_check(self):
        if len(self.languages) > 2:
            self.languages.pop()
        try:
            self.features[self.features.index('Superior Darkvision')] = 'Darkvision'
        except ValueError as err:
            print(err)
        try:
            self.features.remove('Mask of the Wild')
        except ValueError as err:
            print(err)
        try:
            self.other.remove('Rapier')
            self.other.remove('Shortsword')
            self.other.remove('Hand Crossbow')
        except ValueError as err:
            if 'Longbow' not in self.other:
                self.other.extend('Longsword', 'Shortsword', 'Shortbow', 'Longbow')

    def _wood_elf_check(self):
        if len(self.languages) > 2:
            self.languages.pop()
        if 'Mask of the Wild' not in self.features:
            self.features.append('Mask of the Wild')
        try:
            self.features[self.features.index('Superior Darkvision')] = 'Darkvision'
        except ValueError as err:
            print(err)
        try:
            self.other.remove('Rapier')
            self.other.remove('Shortsword')
            self.other.remove('Hand Crossbow')
        except ValueError as err:
            if 'Longbow' not in self.other:
                self.other.extend('Longsword', 'Shortsword', 'Shortbow', 'Longbow')

    def _dark_elf_check(self):
        if len(self.languages) > 2:
            self.languages.pop()
        try:
            self.features[self.features.index('Darkvision')] = 'Superior Darkvision'
        except ValueError as err:
            print(err)
        try:
            self.features.remove('Mask of the Wild')
        except ValueError as err:
            print(err)
        try:
            self.other.remove('Longsword')
            self.other.remove('Shortsword')
            self.other.remove('Shortbow')
            self.other.remove('Longbow')
        except ValueError as err:
            if 'Rapier' not in self.other:
                self.other.extend(['Rapier', 'Shortsword', 'Hand Crossbow'])
