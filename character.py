import json

class Character(object):
    def __init__(self, player_name, stats, race, character_class, background):
        self.race = race
        self.stats = stats
        self.character_class = character_class
        self.background = background
        self._set_header(player_name)
        self._set_proficiencies()
        self._set_prof_mods()
        self._set_hit_points()
        self._set_armor_class()
        self._set_speed()
        self._set_passive_perception()
        self._set_other()
        self._set_features()
        self._set_attacks()
        self.initiative = self.stats.dex_mod

    def _set_header(self, player_name):
        self.character_name = self.background.traits.name
        self.class_name = type(self.character_class).__name__ + ' Lvl 1'
        self.background_name = 'Custom'
        self.player_name = player_name
        self.race_name = type(self.race).__name__
        if self.race.subrace:
            self.race_name = self.race.subrace
        self.alignment = self.background.traits.alignment
        self.experience = '0'

    def _set_proficiencies(self):
        self.proficiencies = []
        self.saving_throws = self.character_class.saving_throws
        self.proficiencies.extend(self.race.proficiencies)
        self.proficiencies.extend(self.character_class.skills)
        self.proficiencies.extend(self.background.skills)

    def _set_prof_mods(self):
        '''Order: Acrobatics, Animal Handling, Athletics, Deception,
        History, Insight, Intimidation, Investigation,
        Arcana, Perception, Nature, Performance,
        Medicine, Religion, Stealth, Persuasion,
        Sleight of Hand, Survival'''
        self.mods = {}
        self.save_mods = {}
        self.mods['Acrobatics'] = self.stats.dex_mod
        self.mods['Animal'] = self.stats.wis_mod
        self.mods['Athletics'] = self.stats.str_mod
        self.mods['Deception'] = self.stats.chr_mod
        self.mods['History'] = self.stats.int_mod
        self.mods['Insight'] = self.stats.wis_mod
        self.mods['Intimidation'] = self.stats.chr_mod
        self.mods['Investigation'] = self.stats.int_mod
        self.mods['Arcana'] = self.stats.int_mod
        self.mods['Perception'] = self.stats.wis_mod
        self.mods['Nature'] = self.stats.int_mod
        self.mods['Performance'] = self.stats.chr_mod
        self.mods['Medicine'] = self.stats.wis_mod
        self.mods['Religion'] = self.stats.int_mod
        self.mods['Stealth'] = self.stats.dex_mod
        self.mods['Persuasion'] = self.stats.chr_mod
        self.mods['SleightofHand'] = self.stats.dex_mod
        self.mods['Survival'] = self.stats.wis_mod
        self.save_mods['Strength'] = self.stats.str_mod
        self.save_mods['Dexterity'] = self.stats.dex_mod
        self.save_mods['Constitution'] = self.stats.con_mod
        self.save_mods['Intelligence'] = self.stats.int_mod
        self.save_mods['Wisdom'] = self.stats.wis_mod
        self.save_mods['Charisma'] = self.stats.chr_mod
        for proficiency in self.proficiencies:
            self.mods[proficiency] += 2
        for save_throw in self.character_class.saving_throws:
            self.save_mods[save_throw] += 2
        self._convert_mods_to_str()

    def _convert_mods_to_str(self):
        for skill in self.mods:
            if self.mods[skill] > 0:
                self.mods[skill] = '+' + str(self.mods[skill])
            elif self.mods[skill] < 0:
                self.mods[skill] = '-' + str(self.mods[skill])
            else:
                self.mods[skill] = str(self.mods[skill])
        for save in self.save_mods:
            if self.save_mods[save] > 0:
                self.save_mods[save] = '+' + str(self.save_mods[save])
            elif self.save_mods[save] < 0:
                self.save_mods[save] = '-' + str(self.save_mods[save])
            else:
                self.save_mods[save] = str(self.save_mods[save])

    def _set_hit_points(self):
        self.hit_points = self.character_class.hit_die + self.stats.con_mod

    def _set_armor_class(self):
        adjusted_dex_mod = self.stats.dex_mod
        if adjusted_dex_mod > 2:
            adjusted_dex_mod = 2
        if 'Light Armor' in self.character_class.equipment:
            self.armor_class = 11 + self.stats.dex_mod
        elif 'Scale Mail' in self.character_class.equipment:
            self.armor_class = 14 + adjusted_dex_mod
        elif 'Chain Mail' in self.character_class.equipment:
            self.armor_class = 16
        else:
            self.armor_class = 10 + self.stats.dex_mod
        for equipment in self.character_class.equipment:
            if 'Shield' in equipment:
                self.armor_class += 2

    def _set_speed(self):
        self.speed = self.race.speed
        if 'Chain Mail' in self.character_class.equipment and self.stats.str < 13:
            self.speed -= 10

    def _set_passive_perception(self):
        self.passive_perception = 10 + self.mods['Perception']

    def _set_other(self):
        self.languages = []
        self.other = []
        self.languages.extend(self.race.languages)
        self.languages.extend(self.background.languages)
        self.other.extend(self.race.other)
        self.other.extend(self.character_class.other)
        self.other.extend(self.background.other)

    def _set_features(self):
        self.features = []
        self.features.extend(self.race.features)
        self.features.extend(self.character_class.features)
        self.features.extend(self.background.features)

    def _set_attacks(self):
        with open('simpleMelee.json') as simple_m, open('simpleRanged.json') as simple_r,\
        open('martialMelee.json') as martial_m, open('martialRanged.json') as martial_r:
            simple_melee = json.load(simple_m)
            simple_ranged = json.load(simple_r)
            martial_melee = json.load(martial_m)
            martial_ranged = json.load(martial_r)

        attacks = [{}, {}, {}]
        count = 0
        for equipment in self.character_class.equipment:
            if count > 2:
                break
            if equipment in simple_melee:
                weapon = self._get_weapon(equipment, simple_melee)
                self._set_melee_stats(attacks, equipment, 'Simple Weapons', weapon, count)
                count += 1
            elif equipment in simple_ranged:
                weapon = self._get_weapon(equipment, simple_ranged)
                self._set_ranged_stats(attacks, equipment, 'Simple Weapons', weapon, count)
                count += 1
            elif equipment in martial_melee:
                weapon = self._get_weapon(equipment, martial_melee)
                self._set_melee_stats(attacks, equipment, 'Martial Weapons', weapon, count)
                count += 1
            elif equipment in martial_ranged:
                weapon = self._get_weapon(equipment, martial_ranged)
                self._set_ranged_stats(attacks, equipment, 'Martial Weapons', weapon, count)
                count += 1

    def _get_weapon(self, name, weapons):
        for weapon in weapons:
            if weapons['Name'] == name:
                return weapon
        return {'Name': 'N/A', 'Damage': 'N/A'}

    def _set_melee_stats(self, info, equipment, weapon_type, weapon, count):
        if equipment+'s' in self.other or weapon_type in self.other:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = str(self.stats.str_mod + 2)
            info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.str_mod)
        else:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = str(self.stats.str_mod)
            info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.str_mod)

    def _set_ranged_stats(self, info, equipment, weapon_type, weapon, count):
        if equipment+'s' in self.other or weapon_type in self.other:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = str(self.stats.dex_mod + 2)
            info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.dex_mod)
        else:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = str(self.stats.dex_mod)
            info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.dex_mod)
