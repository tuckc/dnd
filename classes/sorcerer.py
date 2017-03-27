from char_class import Class

class Sorcerer(Class):
    def __init__(self, skills, equipment, cantrips, spells, origin):
        Class.__init__()
        self.hit_die = 6
        self.other = [
            'Daggers',
            'Darts',
            'Slings',
            'Quarterstaffs',
            'Light Crossbows'
        ]
        #TODO: Think about how to handle sorcerer origin
        self.features = [origin]
        self.saving_throws = ['Constitution', 'Charisma']
        self.skills = skills
        self.equipment = equipment
        self.cantrips = cantrips
        self.spells = spells
