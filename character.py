class Character(object):
    def __init__(self, player_name, stats, race, character_class, background):
        self.player_name = player_name
        self.character_name = background.traits.name
        self.race = type(race).__name__
        self.class_name = type(character_class).__name__ + ' Lvl 1'
        self.background = 'Custom'
        self.experience = '0'
        