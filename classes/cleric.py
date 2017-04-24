from char_class import Class

class Cleric(Class):
    def __init__(self, skills, equipment, cantrips, spells, domain):
        Class.__init__(self)
        self.other = [
            'Light Armor',
            'Medium Armor',
            'Shields'
            'Simple Weapons'
        ]
        self.saving_throws = ['Wisdom', 'Charisma']
        self.features = [domain]
        self.skils = skills
        self.equipment = equipment
        self.cantrips = cantrips
        self.spells = spells
    def __str__(self):
        return super(Cleric, self).__str__()