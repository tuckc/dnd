class Race(object):
    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.speed = 30
        self.languages = []
        self.features = []
        self.other = []
        self.subrace = ''
        self.proficiencies = []
        self.cantrips = []

    def __str__(self):
        return "Strength:{}\nDexterity:{}\nConstitution:{}\nIntelligence:{}\nWisdom:{}\nCharisma:{}\nSpeed:{}\nLanguages:{}\nFeatures:{}\nOther:{}\nSubrace:{}\nProficiences:{}\nCantrips:{}\n".format(self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma,self.speed,self.languages.__str__(),self.features.__str__(),self.other.__str__(),self.subrace,self.proficiencies.__str__(),self.cantrips.__str__())


