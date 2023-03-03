import random


def roll(possibility):
    return random.randint(1, 100) <= possibility


counter = 0
for i in range(100):
    if roll(30):
        counter += 1
print(counter)