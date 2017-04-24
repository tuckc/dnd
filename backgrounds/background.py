from traits import Traits

class Background(object):
    def __init__(self, skills, other, languages, features, traits):
        self.skills = skills
        self.other = other
        self.languages = languages
        self.features = features
        self.personality = traits.personality
        self.ideals = traits.ideals
        self.bonds = traits.bonds
        self.flaws = traits.flaws
        self.name = traits.name
        self.alignment = traits.alignment

    def __str__(self):

        st = "\nSkills: "
        for b in self.skills:
            st += b
            if b != self.skills[-1]:
                st += ", "

        st += "\nFeatures: "
        for b in self.features:
            st += b
            if b != self.features[-1]:
                st += ", "

        st += "\nPersonality: "
        for b in self.personality:
            st += b
            if b != self.personality[-1]:
                st += ", "


        st += "\nIdeals: "
        for b in self.ideals:
            st += b
            if b != self.ideals[-1]:
                st += ", "

        st += "\nBonds: "
        for b in self.bonds:
            st += b
            if b != self.bonds[-1]:
                st += ", "

        st += "\nFlaws: "
        for b in self.flaws:
            st += b
            if b != self.flaws[-1]:
                st += ", "

        st += "\nName:"
        st += self.name

        st += "\nAlignment:"
        st += self.alignment



        return st
        



        ''' st = "Skills:"
        st += self.skills

        st += "\nOther: "
        st += self.other

        st += "\nFeatures: "
        st += self.features

        st += "\nPersonality: "
        st += self.personality

        st += "\nIdeals: "
        st += self.ideals

        st += "\nBonds: "
        st += self.bonds

        st += "\nFlaws: "
        st += self.flaws

        st += "\nName: "
        st += self.name

        st += "\nAlignment: "
        st += self.alignment'''