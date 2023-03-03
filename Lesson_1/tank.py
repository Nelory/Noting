from Lesson_1.character import Character


class Tank(Character):
    def __init__(self, name='', health=100, damage=1, defence=0):
        Character.__init__(self, name, health, damage, defence)

    def take_damage(self, damage):
        self.health -= max(damage - self.defence, 0)