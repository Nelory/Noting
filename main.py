class Character:
    name = ''
    health = 100
    damage = 1
    defence = 1

    def set_name(self, new_name):
        self.name = new_name


player1 = Character()

print(player1.health)

player1.set_name('Ameba')
print(player1.name)