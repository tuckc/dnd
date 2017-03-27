from char_class import Class

class Wizard(Class):
    def __init__(self, skills, equipment, cantrips, spells):
        Class.__init__()
        self.hit_die = 6
        self.other = [
            'Daggers',
            'Darts',
            'Slings',
            'Quarterstaffs',
            'Light Crossbows'
        ]
        self.features = ['Spellbook', 'Arcane Recovery']
        self.saving_throws = ['Intelligence', 'Wisdom']
        self.skills = skills
        self.equipment = equipment
        self.cantrips = cantrips
        self.spells = spells
