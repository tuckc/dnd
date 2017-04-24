class Stats(object):
    def __init__(self, race, strength, dex, con, intel, wis, cha):
        self.strength = strength + race.strength
        self.dexterity = dex + race.dexterity
        self.constitution = con + race.constitution
        self.intelligence = intel + race.intelligence
        self.wisdom = wis + race.wisdom
        self.charisma = cha + race.charisma
        self._calculate_modifiers()

    def _calculate_modifiers(self):
        self.str_mod = (self.strength - 10) / 2
        self.dex_mod = (self.dexterity - 10) / 2
        self.con_mod = (self.constitution - 10) / 2
        self.int_mod = (self.intelligence - 10) / 2
        self.wis_mod = (self.wisdom - 10) / 2
        self.chr_mod = (self.charisma - 10) / 2

    
    def __str__(self):
        st = "Strength: "+ self.strength.__str__()
        st += "\nDexterity: "+ self.dexterity.__str__()
        st += "\nConstitution: "+ self.constitution.__str__()
        st += "\nIntelligence: "+ self.intelligence.__str__()
        st += "\nWisdom: "+ self.wisdom.__str__()
        st += "\nCharisma: "+ self.charisma.__str__()
        return st

