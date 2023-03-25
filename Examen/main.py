from Examen import person

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

go_to_park = Action(name = 'Сходить в парк', money = 0, mood = 15, health = 3)
human.do(go_to_park)
print(human)

# === Тарас ===
# Здоровье: 103
# Настроение: 115
# Капитал: 0
