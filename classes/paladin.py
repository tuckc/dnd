from char_class import Class

class Paladin(Class):
    def __init__(self, skills, equipment):
        Class.__init__()
        self.other = [
            'All Armor',
            'Shields',
            'Simple Weapons',
            'Martial Weapons'
        ]
        self.features = ['Divine Sense', 'Lay on Hands']
        self.saving_throws = ['Wisdom', 'Charisma']
        self.skills = skills
        self.equipment = equipment
        