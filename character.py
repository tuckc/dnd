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
        self._set_other()
        self._set_features()
        self._set_attacks()
        self.initiative = self.stats.dex_mod
        self._set_spells()

    def _set_header(self, player_name):
        self.character_name = self.background.name
        self.class_name = type(self.character_class).__name__ + ' Lvl 1'
        self.background_name = 'Custom'
        self.player_name = player_name
        self.race_name = type(self.race).__name__
        if self.race.subrace:
            self.race_name = self.race.subrace
        self.alignment = self.background.alignment
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
        self.mods['Animal Handling'] = self.stats.wis_mod
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
        self.mods['Sleight of Hand'] = self.stats.dex_mod
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
        self._set_passive_perception()
        self._convert_mods_to_str()

    def _set_passive_perception(self):
        self.passive_perception = 10 + self.mods['Perception']

    def _convert_mods_to_str(self):
        for skill in self.mods:
            if self.mods[skill] > 0:
                self.mods[skill] = '+' + str(self.mods[skill])
            else:
                self.mods[skill] = str(self.mods[skill])
        for save in self.save_mods:
            if self.save_mods[save] > 0:
                self.save_mods[save] = '+' + str(self.save_mods[save])
            else:
                self.save_mods[save] = str(self.save_mods[save])
        self.passive_perception = str(self.passive_perception)

    def _set_hit_points(self):
        self.hit_points = str(self.character_class.hit_die + self.stats.con_mod)

    def _set_armor_class(self):
        adjusted_dex_mod = self.stats.dex_mod
        if adjusted_dex_mod > 2:
            adjusted_dex_mod = 2
        if 'Leather Armor' in self.character_class.equipment:
            self.armor_class = 11 + self.stats.dex_mod
        elif 'Scale Mail' in self.character_class.equipment:
            self.armor_class = 14 + adjusted_dex_mod
        elif 'Chain Mail' in self.character_class.equipment:
            self.armor_class = 16
        else:
            self.armor_class = 10 + self.stats.dex_mod
        if 'Shield' in self.character_class.equipment:
            self.armor_class += 2
        self.armor_class = str(self.armor_class)

    def _set_speed(self):
        self.speed = self.race.speed
        if 'Chain Mail' in self.character_class.equipment and self.stats.strength < 13:
            self.speed -= 10
        self.speed = str(self.speed)

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
        with open('../simpleMelee.json') as simple_m, open('../simpleRanged.json') as simple_r,\
        open('../martialMelee.json') as martial_m, open('../martialRanged.json') as martial_r:
            simple_melee = json.load(simple_m)
            simple_ranged = json.load(simple_r)
            martial_melee = json.load(martial_m)
            martial_ranged = json.load(martial_r)

        self.attacks = [{}, {}, {}]
        count = 0
        for equipment in self.character_class.equipment:
            if count > 2:
                break
            if equipment in [wep['Name'] for wep in simple_melee]:
                weapon = self._get_weapon(equipment, simple_melee)
                self._set_melee_stats(self.attacks, equipment, 'Simple Weapons', weapon, count)
                count += 1
            elif equipment in [wep['Name'] for wep in simple_ranged]:
                weapon = self._get_weapon(equipment, simple_ranged)
                self._set_ranged_stats(self.attacks, equipment, 'Simple Weapons', weapon, count)
                count += 1
            elif equipment in [wep['Name'] for wep in martial_melee]:
                weapon = self._get_weapon(equipment, martial_melee)
                self._set_melee_stats(self.attacks, equipment, 'Martial Weapons', weapon, count)
                count += 1
            elif equipment in [wep['Name'] for wep in martial_ranged]:
                weapon = self._get_weapon(equipment, martial_ranged)
                self._set_ranged_stats(self.attacks, equipment, 'Martial Weapons', weapon, count)
                count += 1

    def _get_weapon(self, name, weapons):
        for weapon in weapons:
            if weapon['Name'] == name:
                return weapon
        return {'Name': 'N/A', 'Damage': 'N/A'}

    def _set_melee_stats(self, info, equipment, weapon_type, weapon, count):
        if equipment+'s' in self.other or weapon_type in self.other:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = '+' + str(self.stats.str_mod + 2) if self.stats.str_mod + 2 > 0 else self.stats.str_mod
            if self.stats.str_mod >= 0:
                info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.str_mod)
            else:
                info[count]['Damage'] = weapon['Damage'] + str(self.stats.str_mod)
        else:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = '+' + str(self.stats.str_mod) if self.stats.str_mod > 0 else self.stats.str_mod
            if self.stats.str_mod >= 0:
                info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.str_mod)
            else:
                info[count]['Damage'] = weapon['Damage'] + str(self.stats.str_mod)

    def _set_ranged_stats(self, info, equipment, weapon_type, weapon, count):
        if equipment+'s' in self.other or weapon_type in self.other:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = '+' + str(self.stats.dex_mod + 2) if self.stats.dex_mod + 2 > 0 else self.stats.dex_mod
            if self.stats.dex_mod >= 0:
                info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.dex_mod)
            else:
                info[count]['Damage'] = weapon['Damage'] + str(self.stats.dex_mod)
        else:
            info[count]['Name'] = weapon['Name']
            info[count]['AtkBonus'] = '+' + str(self.stats.dex_mod) if self.stats.dex_mod > 0 else self.stats.dex_mod
            if self.stats.dex_mod >= 0:
                info[count]['Damage'] = weapon['Damage'] + '+' + str(self.stats.dex_mod)
            else:
                info[count]['Damage'] = weapon['Damage'] + str(self.stats.dex_mod)

    def _set_spells(self):
        self.spells = []
        self.spells.extend(self.race.cantrips)
        self.spells.extend(self.character_class.cantrips)
        self.spells.extend(self.character_class.spells)

    def get_form_fields(self):
        all_fields = []
        all_fields.append(('ClassLevel', self.class_name))
        all_fields.append(('Background', self.background_name))
        all_fields.append(('PlayerName', self.player_name))
        all_fields.append(('CharacterName', self.character_name))
        all_fields.append(('Race ', self.race_name))
        all_fields.append(('Alignment', self.alignment))
        all_fields.append(('XP', self.experience))
        all_fields.append(('STR', self.stats.strength))
        all_fields.append(('ProfBonus', '+2'))
        all_fields.append(('AC', self.armor_class))
        all_fields.append(('Initiative', '+' + str(self.initiative) if self.initiative > 0 else str(self.initiative)))
        all_fields.append(('Speed', self.speed))
        all_fields.append(('PersonalityTraits ', self.background.personality))
        all_fields.append(('STRmod', '+' + str(self.stats.str_mod) if self.stats.str_mod > 0 else self.stats.str_mod))
        all_fields.append(('HPMax', self.hit_points))
        all_fields.append(('ST Strength', self.save_mods['Strength']))
        all_fields.append(('DEX', self.stats.dexterity))
        all_fields.append(('HPCurrent', self.hit_points))
        all_fields.append(('Ideals', self.background.ideals))
        all_fields.append(('DEXmod ', '+' + str(self.stats.dex_mod) if self.stats.dex_mod > 0 else self.stats.dex_mod))
        all_fields.append(('Bonds', self.background.bonds))
        all_fields.append(('CON', self.stats.constitution))
        all_fields.append(('HDTotal', '1'))
        all_fields.append(('CONmod', '+' + str(self.stats.con_mod) if self.stats.con_mod > 0 else self.stats.con_mod))
        all_fields.append(('HD', '1d' + str(self.character_class.hit_die)))
        all_fields.append(('Flaws', self.background.flaws))
        all_fields.append(('INT', self.stats.intelligence))
        all_fields.append(('ST Dexterity', self.save_mods['Dexterity']))
        all_fields.append(('ST Constitution', self.save_mods['Constitution']))
        all_fields.append(('ST Intelligence', self.save_mods['Intelligence']))
        all_fields.append(('ST Wisdom', self.save_mods['Wisdom']))
        all_fields.append(('ST Charisma', self.save_mods['Charisma']))
        all_fields.append(('Acrobatics', self.mods['Acrobatics']))
        all_fields.append(('Animal', self.mods['Animal Handling']))
        all_fields.append(('Athletics', self.mods['Athletics']))
        all_fields.append(('Deception ', self.mods['Deception']))
        all_fields.append(('History ', self.mods['History']))
        all_fields.append(('Insight', self.mods['Insight']))
        all_fields.append(('Intimidation', self.mods['Intimidation']))
        all_fields.append(('Check Box 11', True if 'Strength' in self.character_class.saving_throws else False))
        all_fields.append(('Check Box 18', True if 'Dexterity' in self.character_class.saving_throws else False))
        all_fields.append(('Check Box 19', True if 'Constitution' in self.character_class.saving_throws else False))
        all_fields.append(('Check Box 20', True if 'Intelligence' in self.character_class.saving_throws else False))
        all_fields.append(('Check Box 21', True if 'Wisdom' in self.character_class.saving_throws else False))
        all_fields.append(('Check Box 22', True if 'Charisma' in self.character_class.saving_throws else False))
        all_fields.append(('Wpn Name', self.attacks[0]['Name'] if self.attacks[0] else ''))
        all_fields.append(('Wpn1 AtkBonus', self.attacks[0]['AtkBonus'] if self.attacks[0] else ''))
        all_fields.append(('Wpn1 Damage', self.attacks[0]['Damage'] if self.attacks[0] else ''))
        all_fields.append(('INTmod', '+' + str(self.stats.int_mod) if self.stats.int_mod > 0 else self.stats.int_mod))
        all_fields.append(('Wpn Name 2', self.attacks[1]['Name'] if self.attacks[1] else ''))
        all_fields.append(('Wpn2 AtkBonus ', self.attacks[1]['AtkBonus'] if self.attacks[1] else ''))
        all_fields.append(('Wpn2 Damage ', self.attacks[1]['Damage'] if self.attacks[1] else ''))
        all_fields.append(('Investigation ', self.mods['Investigation']))
        all_fields.append(('WIS', self.stats.wisdom))
        all_fields.append(('Wpn Name 3', self.attacks[2]['Name'] if self.attacks[2] else ''))
        all_fields.append(('Wpn3 AtkBonus', self.attacks[2]['AtkBonus'] if self.attacks[2] else ''))
        all_fields.append(('Wpn3 Damage', self.attacks[2]['Damage'] if self.attacks[2] else ''))
        all_fields.append(('Arcana', self.mods['Arcana']))
        all_fields.append(('Perception ', self.mods['Perception']))
        all_fields.append(('WISmod', '+' + str(self.stats.wis_mod) if self.stats.wis_mod > 0 else self.stats.wis_mod))
        all_fields.append(('CHA', self.stats.charisma))
        all_fields.append(('Nature', self.mods['Nature']))
        all_fields.append(('Performance', self.mods['Performance']))
        all_fields.append(('Medicine', self.mods['Medicine']))
        all_fields.append(('Religion', self.mods['Religion']))
        all_fields.append(('Stealth ', self.mods['Stealth']))
        all_fields.append(('Check Box 23', True if 'Acrobatics' in self.proficiencies else False))
        all_fields.append(('Check Box 24', True if 'Animal Handling' in self.proficiencies else False))
        all_fields.append(('Check Box 25', True if 'Arcana' in self.proficiencies else False))
        all_fields.append(('Check Box 26', True if 'Athletics' in self.proficiencies else False))
        all_fields.append(('Check Box 27', True if 'Deception' in self.proficiencies else False))
        all_fields.append(('Check Box 28', True if 'History' in self.proficiencies else False))
        all_fields.append(('Check Box 29', True if 'Insight' in self.proficiencies else False))
        all_fields.append(('Check Box 30', True if 'Intimidation' in self.proficiencies else False))
        all_fields.append(('Check Box 31', True if 'Investigation' in self.proficiencies else False))
        all_fields.append(('Check Box 32', True if 'Medicine' in self.proficiencies else False))
        all_fields.append(('Check Box 33', True if 'Nature' in self.proficiencies else False))
        all_fields.append(('Check Box 34', True if 'Perception' in self.proficiencies else False))
        all_fields.append(('Check Box 35', True if 'Performance' in self.proficiencies else False))
        all_fields.append(('Check Box 36', True if 'Persuasion' in self.proficiencies else False))
        all_fields.append(('Check Box 37', True if 'Religion' in self.proficiencies else False))
        all_fields.append(('Check Box 38', True if 'Sleight of Hand' in self.proficiencies else False))
        all_fields.append(('Check Box 39', True if 'Stealth' in self.proficiencies else False))
        all_fields.append(('Check Box 40', True if 'Survival' in self.proficiencies else False))
        all_fields.append(('Persuasion', self.mods['Persuasion']))
        all_fields.append(('SleightofHand', self.mods['Stealth']))
        all_fields.append(('CHamod', '+' + str(self.stats.chr_mod) if self.stats.chr_mod > 0 else self.stats.chr_mod))
        all_fields.append(('Survival', self.mods['Survival']))
        all_fields.append(('AttacksSpellcasting', '\n'.join(self.spells)))
        all_fields.append(('Passive', self.passive_perception))
        languages = ', '.join(self.languages)
        other = ', '.join(self.other)
        both = languages + '\n\n' + other
        all_fields.append(('ProficienciesLang', languages + '\n\n' + other))
        all_fields.append(('Equipment', '\n'.join(self.character_class.equipment)))
        all_fields.append(('Features and Traits', '\n'.join(self.features)))

        return all_fields


    def __str__(self):
        st = "Race: " + self.race_name
        st += "\nStrength: "+ self.stats.strength.__str__()
        st += "\nDexterity: "+ self.stats.dexterity.__str__()
        st += "\nConstitution: "+ self.stats.constitution.__str__()
        st += "\nIntelligence: "+ self.stats.intelligence.__str__()
        st += "\nWisdom: "+ self.stats.wisdom.__str__()
        st += "\nCharisma: "+ self.stats.charisma.__str__()
        st += "\nSpeed: "+ self.speed.__str__()

        st += "\nLanguages: "
        for a in self.languages:
            st += a
            if a != self.languages[-1]:
                st += ", "

        st += "\nFeatures: "
        for b in self.features:
            st += b
            if b != self.features[-1]:
                st += ", "

        st += "\nOther: "
        for b in self.other:
            st += b
            if b != self.other[-1]:
                st += ", "

        st += "\nSubrace: "
        st += self.race.subrace

        st += "\nProficiencies: "
        for b in self.proficiencies:
            st += b
            if b != self.proficiencies[-1]:
                st += ", "

        st += "\nAttacks: "
        for b in self.attacks:
            for a in b.keys():
                st += b[a]
                st += "  "
            

        st += "\nBackground:"
        st += self.background.__str__()

        st += "\nHit Die: "+ self.character_class.hit_die.__str__()
        

        st += "\nHit Points:"
        st += self.hit_points

        st += "\nArmor Class:"
        st += self.armor_class.__str__()

        st += "\nInitiative:"
        st += str(self.initiative)

        st += "\nOther: "
        for a in self.other:
            st += a
            if a != self.other[-1]:
                st += ", "



        st += "\nSaving Throws: "
        for b in self.saving_throws:
            st += b
            if b != self.saving_throws[-1]:
                st += ", "

        st += "\nEquipment: "
        for b in self.character_class.equipment:
            st += b
            if b != self.character_class.equipment[-1]:
                st += ", "

        st += "\nSpells: "
        for b in self.spells:
            st += b
            if b != self.spells[-1]:
                st += ", "
        return st
        
        