from Lesson_1.character import Character


class Berserk (Character):
    def __init__(self, name='', health=100, damage=1, defence=0):
        Character.__init__(self, name, health, damage, defence)

        self.additional_damage = 0
        self.max_health = health

    def take_damage(self, damage):
        super(Berserk, self).take_damage(damage=damage)

    def attack(self, enemy):
        self.additional_damage = \
            max(
                (1 - self.health / self.max_health) * self.damage,
                0
            )

        enemy.take_damage(self.damage + self.additional_damage)