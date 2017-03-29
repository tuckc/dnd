from char_class import Class

class Bard(Class):
    def __init__(self, skills, equipment, instruments, cantrips, spells):
        Class.__init__(self)
        self.other = [
            'Light Armor',
            'Simple Weapons',
            'Hand Crossbows',
            'Longswords',
            'Rapiers',
            'Shortswords'
        ]
        self.other.extend(instruments)
        self.features = ['Bardic Inspiration (d6)']
        self.saving_throws = ['Dexterity', 'Charisma']
        self.skills = skills
        self.equipment = equipment
        self.cantrips = cantrips
        self.spells = spells
