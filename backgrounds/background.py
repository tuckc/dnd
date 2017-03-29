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
        