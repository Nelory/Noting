from character import Character

player1 = Character(name='Ameba', damage=3)
player2 = Character(name= 'Anton', health=150)

print(f' - Player1 - \n{player1}')
print(f' - Player2 - \n{player2}')

player1.attack(player2)
print('Player 1  attacked  Player 2')
player2.attack(player1)
print('Player 2  attacked  Player 1')

print(f' - Player1 - \n{player1}')
print(f' - Player2 - \n{player2}')