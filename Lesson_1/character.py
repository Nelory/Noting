class Character:
    name = ''
    health = 100
    damage = 1
    defence = 1

    def __int__(self, name='', health=100, damage=1, defence=0):
        pass
    def set_name(self, new_name):
        self.name = new_name