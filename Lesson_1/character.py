class Character:
    name = ''
    health = 100
    damage = 1
    group = 11
    age = 18
    average_mark = 11

    def __init__(self, name='', health=100, damage=1, age=18, group=11,average_mark = 11):
        self.name = name
        self.health = health
        self.damage = damage


    def __str__(self):
        return \
            f'Name: {self.name}\n' \
            f'Health: {self.health}\n' \
            f'Damage: {self.damage}\n' \
            f'Group: {self.group}\n' \
            f'Average_mark: {self.average_mark}\n' \
            f'Age: {self.age}\n'

    def take_damage(self, damage):
        self.health -= max(damage, 0)

    def attack(self, enemy):
        enemy.take_damage(self.damage)

    def set_name(self, new_name):
        self.name = new_name

    def get_age(self, new_age):
        self.age = new_age

