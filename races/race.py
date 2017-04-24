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
        st = "Strength: "+ self.strength.__str__()
        st += "\nDexterity: "+ self.dexterity.__str__()
        st += "\nConstitution: "+ self.constitution.__str__()
        st += "\nIntelligence: "+ self.intelligence.__str__()
        st += "\nWisdom: "+ self.wisdom.__str__()
        st += "\nCharisma: "+ self.charisma.__str__()
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

        st += "Subrace: "
        st += self.subrace

        st += "\nProficiencies: "
        for b in self.proficiencies:
            st += b
            if b != self.proficiencies[-1]:
                st += ", "

        st += "\nCantrips: "
        for b in self.cantrips:
            st += b
            if b != self.cantrips[-1]:
                st += ", "


        return st
        #return "Strength:{}\nDexterity:{}\nConstitution:{}\nIntelligence:{}\nWisdom:{}\nCharisma:{}\nSpeed:{}\nLanguages:{}\nFeatures:{}\nOther:{}\nSubrace:{}\nProficiences:{}\nCantrips:{}\n".format(self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma,self.speed,self.languages.__str__(),self.features.__str__(),self.other.__str__(),self.subrace,self.proficiencies.__str__(),self.cantrips.__str__())


