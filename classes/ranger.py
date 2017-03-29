from char_class import Class

class Ranger(Class):
    def __init__(self, skills, equipment):
        Class.__init__(self)
        self.hit_die = 10
        self.other = [
            'Light Armor',
            'Medium Armor',
            'Shields',
            'Simple Weapons',
            'Martial Weapons'
        ]
        #TODO Implement Favored Enemy?
        self.features = ['Favored Enemy', 'Natural Explorer']
        self.saving_throws = ['Strength', 'Dexterity']
        self.skills = skills
        self.equipment = equipment
        