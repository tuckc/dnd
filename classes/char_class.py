class Class(object):
    def __init__(self):
        self.hit_die = 8
        self.hit_points = 0
        self.other = []
        self.features = []
        self.saving_throws = []
        self.skills = []
        self.equipment = []
        self.cantrips = []
        self.spells = []

    def calculate_hit_points(self, modifier):
        self.hit_points = self.hit_die + modifier
