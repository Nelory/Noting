import random


def roll(possibility):
    return random.randint(1,5) <= possibility


counter = 0
for i in range(1):
    if roll(1):
        counter += 1000
    else:
        counter += 8
print(counter)