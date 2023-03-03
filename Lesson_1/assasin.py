from Lesson_1.character import Character
from Lesson3.possibility import counter

class Assasin(Character):
    def __init__(self, name='', health=115, damage=counter, defence=0):
        Character.__init__(self, name, health, damage, defence)
