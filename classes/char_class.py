class Class(object):
    def __init__(self):
        self.hit_die = 8
        self.hit_points = 0
        self.armor_class = 0
        self.other = []
        self.features = []
        self.saving_throws = []
        self.skills = []
        self.equipment = []
        self.cantrips = []
        self.spells = []

    def calculate_hit_points(self, modifier):
        self.hit_points = self.hit_die + modifier

    def calculate_armor_class(self, modifier, light, medium, heavy, shield):
        if light:
            self.armor_class = 11 + modifier
        elif medium:
            self.armor_class = 14 + modifier
        elif heavy:
            self.armor_class = 16
        else:
            self.armor_class = 10 + modifier
        if shield:
            self.armor_class += 2
