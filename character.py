class Character(object):
    def __init__(self, player_name, stats, race, character_class, background):
        self._set_header(background, character_class, race, player_name)
        self.stats = stats
        self.saving_throws = character_class.saving_throws
        self._set_proficiencies(race, character_class, background)
        self._set_prof_mods()

    def _set_header(self, background, character_class, race, player_name):
        self.character_name = background.traits.name
        self.class_name = type(character_class).__name__ + ' Lvl 1'
        self.background = 'Custom'
        self.player_name = player_name
        self.race = type(race).__name__
        self.alignment = background.traits.alignment
        self.experience = '0'

    def _set_proficiencies(self, race, character_class, background):
        self.proficiencies = []
        self.proficiencies.extend(race.proficiencies)
        self.proficiencies.extend(character_class.proficiencies)
        self.proficiencies.extend(background.proficiencies)

    def _set_prof_mods(self):
        '''Order: Acrobatics, Animal, Athletics, Deception,
        History, Insight, Intimidation, Investigation,
        Arcana, Perception, Nature, Performance,
        Medicine, Religion, Stealth, Persuasion,
        SleightofHand, Survival'''
        self.mods = {}
        proficiencies = [
            'Acrobatics',
            'Animal Handling',
            'Athletics',
            'Deception',
            'History',
            'Insight',
            'Intimidation',
            'Investigation',
            'Arcana',
            'Perception',
            'Nature',
            'Performance',
            'Medicine',
            'Religion',
            'Stealth',
            'Persuasion',
            'Sleight of Hand',
            'Survival'
        ]
        for proficiency in proficiencies:
            if proficiency in self.proficiencies:
                if proficiency is 'Sleight of Hand':
                    self.mods['SleightofHand'] = 2
                else:
                    self.mods[proficiency.split(' ', 1)[0]] = 2
            else:
                if proficiency is 'Sleight of Hand':
                    self.mods['SleightofHand'] = 0
                else:
                    self.mods[proficiency.split(' ', 1)[0]] = 0
        self._add_mods()

    def _add_mods(self):
        self.mods['Acrobatics'] += self.stats.dex_mod
        self.mods['Animal'] += self.stats.wis_mod
        self.mods['Athletics'] += self.stats.str_mod
        self.mods['Deception'] += self.stats.chr_mod
        self.mods['History'] += self.stats.int_mod
        self.mods['Insight'] += self.stats.wis_mod
        self.mods['Intimidation'] += self.stats.chr_mod
        self.mods['Investigation'] += self.stats.int_mod
        self.mods['Arcana'] += self.stats.int_mod
        self.mods['Perception'] += self.stats.wis_mod
        self.mods['Nature'] += self.stats.int_mod
        self.mods['Performance'] += self.stats.chr_mod
        self.mods['Medicine'] += self.stats.wis_mod
        self.mods['Religion'] += self.stats.int_mod
        self.mods['Stealth'] += self.stats.dex_mod
        self.mods['Persuasion'] += self.stats.chr_mod
        self.mods['SleightofHand'] += self.stats.dex_mod
        self.mods['Survival'] += self.stats.wis_mod
