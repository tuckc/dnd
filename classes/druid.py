from char_class import Class

class Druid(Class):
    def __init__(self, skills, equipment, cantrips, spells):
        Class.__init__(self)
        self.other = [
            'Light Armor (non-metal)',
            'Medium Armor (non-metal)',
            'Shields (non-metal)',
            'Clubs',
            'Daggers',
            'Darts',
            'Javelins',
            'Maces',
            'Quarterstaffs',
            'Scimitars',
            'Sickles',
            'Slings',
            'Spears',
            'Herbalism Kit'
        ]
        self.features = ['Druidic']
        self.saving_throws = ['Intelligence', 'Wisdom']
        self.skills = skills
        self.equipment = equipment
        self.cantrips = cantrips
        self.spells = spells
    def __str__(self):
        return super(Druid, self).__str__()
        