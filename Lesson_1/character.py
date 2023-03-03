class Character:
    name = ''
    health = 100
    damage = 1
    defence = 0

    # Конструктор
    def __init__(self, name='', health=100, damage=1, defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defence = defence

    def __str__(self):
        return \
            f'Name: {self.name}\n' \
            f'Health: {self.health}\n' \
            f'Damage: {self.damage}\n' \
            f'Defence: {self.defence}\n'

    def take_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, enemy):
        enemy.take_damage(self.damage)

    def set_name(self, new_name):
        self.name = new_name

    def is_alive(self):
        return self.health > 0