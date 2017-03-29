from char_class import Class

class Fighter(Class):
    def __init__(self, skills, equipment, fight_style):
        Class.__init__(self)
        self.hit_die = 10
        self.other = [
            'All Armor',
            'Shields',
            'Simple Weapons',
            'Martial Weapons'
        ]
        self.features = [fight_style, 'Second Wind']
        self.saving_throws = ['Strength', 'Constitution']
        self.skills = skills
        self.equipment = equipment
        