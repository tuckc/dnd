from char_class import Class

class Warlock(Class):
    def __init__(self, skills, equipment, cantrips, spells, patron):
        Class.__init__(self)
        self.other = [
            'Light Armor',
            'Simple Weapons'
        ]
        self.features = ['Otherworldly Patron: ' + patron]
        self.saving_throws = ['Wisdom', 'Charisma']
        self.skills = skills
        self.equipment = equipment
        self.cantrips = cantrips
        self.spells = spells
        