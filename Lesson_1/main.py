from character import Character

player1 = Character(name='Ameba', damage=3)
print(player1.health)

player1.set_name('Ameba')
print(player1.name)

print(player1)

player1.take_damage(10)

print(player1)