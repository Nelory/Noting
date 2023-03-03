from character import Character

player1 = Character(name='Vasya', damage=3)
player2 = Character(name='Petya', health=150)

print(f' - Player 1 - \n{player1}')
print(f' - Player 2 - \n{player2}')

while player1.is_alive() and player2.is_alive():
    player1.attack(player2)
    # player2.health -= max(player1.damage, 0)
    print('Player 1 attacted Player 2')
    player2.attack(player1)
    print('Player 2 attacted Player 1')

    print(f' - Player 1 - \n{player1}')
    print(f' - Player 2 - \n{player2}')
    print('\n\n')