from Lesson_1.character import Character

class Berserk(Character):
    def __init__(self, name='', health=100, damage=1, age=18, group=11, average_mark=11):
        Character.__init__(self, name, health, damage, age, group, average_mark)

        self.additional_damage = 0
        self.max_heals = health

    def take_damage(self, enemy):
        super(Berserk, self).take_damage(damage=damage)

        self.additional_damage = \
            max(
                (1 - self.max_heals / self.max_heals) * self.damage,
                0
            )
        enemy.take_damage(self.damage + self.additional_damage)