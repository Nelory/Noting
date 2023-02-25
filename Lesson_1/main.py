from character import Character
from student import Student

player1 = Character(name='Ameba', damage=3)
Student = Student(name='Anton', health=150,damage=10000, age=2004, group=11, average_mark=11)

print(f' - Player1 - \n{player1}')
print(f' - student.py - \n{Student}')

player1.attack(Student)
print('Player 1  attacked  Player 2')
Student.attack(player1)
print('student.py  attacked  Player 1')

print(f' - Player1 - \n{player1}')
print(f' - student.py - \n{Student}')
