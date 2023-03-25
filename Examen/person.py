import random

class Person:
    health = 100
    mood = 100
    money = 10
    name = ''

    def __init__(self, health=100, mood=100, money=0, name=''):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money
    def __str__(self):
        return \
            f'Name: {self.name}\n' \
            f' здоровье: {self.health}\n' \
            f' деньги: {self.money}\n' \
            f' настроение: {self.mood}\n'

    def change_state(self, money, health, mood):
        self.money += money
        self.health += health
        self.mood += mood




human = Person(name = 'Тарас', money = 0, mood = 100, health = 100)
human.change_state(
        money = random.randint(50, 100),
        mood = random.randint(-20, -10),
        health = random.randint(-10, -5)
    )
print(human)

human = Person(name = 'Тарас', money = 0, mood = 100, health = 100)
print(human)
# === Тарас ===
# Здоровье: 100
# Настроение: 100
# Капитал: 0



class Action(Person):

    health = 100
    mood = 100
    money = 10
    name = ''

    def __init__(self, health=100, mood=100, money=0, name=''):
        Person.__init__(self, money, mood)

    def do(self, money, health, mood, name):
        self.name=name
        self.money += money
        self.health += health
        self.mood += mood

go_to_hospital = Action(name = 'Пойти в больницу', money = 100, mood = 100, health = 100)

go_to_hospital.do(
        name='Пойти в больницу',
        money=-20,
        mood=-5,
        health=20
    )

print(go_to_hospital)

class Rest(Person):

    health = 100
    mood = 100
    money = 10
    name = ''

    def __init__(self, health=100, mood=100, money=0, name=''):
        Person.__init__(self, money, mood)

    def do(self, money, health, mood, name):
        self.name=name
        self.money += money
        self.health += health
        self.mood += mood

go_to_park = Rest(name = 'Сходить в парк', money = 100, mood = 100, health = 100)

go_to_park.do(
        name = 'Сходить в парк',
        money=0,
        mood=15,
        health=3
    )

print(go_to_park)

class Work(Person):

    health = 100
    mood = 100
    money = 10
    name = ''

    def __init__(self, health=100, mood=100, money=0, name=''):
        Person.__init__(self, money, mood)

    def do(self, money, health, mood, name):
        self.name=name
        self.money += money
        self.health += health
        self.mood += mood

go_to_factory = Work(name = 'Пойти на завод', money = 100, mood = 100, health = 100)

go_to_factory.do(
        name='Пойти на завод',
        money=50,
        mood=-10,
        health=-3
    )

print(go_to_factory)




# === Тарас ===
# Здоровье: 103
# Настроение: 115
# Капитал: 0
