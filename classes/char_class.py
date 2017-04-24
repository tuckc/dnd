class Class(object):
    def __init__(self):
        self.hit_die = 8
        self.other = []
        self.features = []
        self.saving_throws = []
        self.skills = []
        self.equipment = []
        self.cantrips = []
        self.spells = []

    def __str__(self):
        st = "Hit Die: "+ self.hit_die.__str__()
        st += "\nOther: "
        for a in self.other:
            st += a
            if a != self.other[-1]:
                st += ", "

        st += "\nFeatures: "
        for b in self.features:
            st += b
            if b != self.features[-1]:
                st += ", "

        st += "\nSaving Throws: "
        for b in self.saving_throws:
            st += b
            if b != self.saving_throws[-1]:
                st += ", "

        st += "\nSkills: "
        for b in self.skills:
            st += b
            if b != self.skills[-1]:
                st += ", "

        st += "\nEquipment: "
        for b in self.equipment:
            st += b
            if b != self.equipment[-1]:
                st += ", "

        st += "\nCantrips: "
        for b in self.cantrips:
            st += b
            if b != self.cantrips[-1]:
                st += ", "

        st += "\nSpells: "
        for b in self.spells:
            st += b
            if b != self.spells[-1]:
                st += ", "
        return st

#return "Hit Die:{}\nOther:{}\nFeatures:{}\nSaving Throws:{}\nSkills:{}\nEquipment:{}\nCantrips:{}\nSpells:{}".format(self.hit_die,self.other.__str__(), self.features.__str__(), self.saving_throws.__str__(), self.skills.__str__(), self.equipment.__str__(),self.cantrips.__str__(), self.spells.__str__())



