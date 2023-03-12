class NotEnoughHealth(BaseException):
    def __init__(self, message=''):
        BaseException.__init__(self, message)
        self.message = message

    def __str__(self):
        return self.message

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


    def attack(self, enemy):
        enemy.take_damage(self.damage)

    def set_name(self, new_name):
        self.name = new_name

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= max(damage, 0)

        if self.health < 0:
            raise NotEnoughHealth(' NO HP!')



character = Character(100, 100)
print(character)



while True:
    try:
        character.take_damage(100)
    except NotEnoughHealth:
        print('HEALTH END')
        break
    else:
        print(character)
