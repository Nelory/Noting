class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

    def __init__(self, name='', health=100, damage=1, defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence
    def set_name(self, new_name):
        self.name = new_name
