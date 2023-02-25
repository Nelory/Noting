from character import Character

player1 = Character(name='Ameba', damage=3)
Student = Character(name= 'Student', health=150,damage=10000, age=2004, group=11, average_mark=11)

print(f' - Player1 - \n{player1}')
print(f' - Student - \n{Student}')

player1.attack(Student)
print('Player 1  attacked  Player 2')
Student.attack(player1)
print('Student  attacked  Player 1')

print(f' - Player1 - \n{player1}')
if Character.health >=0:
    print("He died")
else:
    print("He alive")

print(f' - Student - \n{Student}')

if Character.health <=0:
    print("He died")
else:
    print("He alive")