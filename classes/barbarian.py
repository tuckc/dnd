from char_class import Class

class Barbarian(Class):
    def __init__(self, skills, equipment):
        Class.__init__(self)
        self.hit_die = 12
        self.other = [
            'Light Armor',
            'Medium Armor',
            'Shields',
            'Simple Weapons',
            'Martial Weapons'
        ]
        self.features = ['Rage', 'Unarmored Defense']
        self.saving_throws = ['Strength', 'Constitution']
        self.skills = skills
        self.equipment = equipment
