from Lesson_1.character import Character
from berserk import Berserk

player1 = Character(name='Ameba', damage=10)
Student = Berserk(name='Anton', damage=10)

print(f' - Player1 - \n{player1}')
print(f' - student.py - \n{Student}')

player1.attack(Student)
print('Player 1  attacked  Player 2')
Student.attack(player1)
print('student.py  attacked  Player 1')

print(f' - Player1 - \n{player1}')
print(f' - student.py - \n{Student}')
print('\n\n')
