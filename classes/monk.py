from char_class import Class

class Monk(Class):
    def __init__(self, skills, equipment, tool):
        Class.__init__()
        self.other = [
            'Simple Weapons',
            'Shortswords',
            tool
        ]
        self.features = ['Unarmored Defense', 'Martial Arts']
        self.saving_throws = ['Strength', 'Dexterity']
        self.skills = skills
        self.equipment = equipment
        