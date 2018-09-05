from random import randint

class Dice():

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1, self.sides)

d6 = Dice()
results = []

results = []
for roll_num in range(10):
    result = d6.roll_dice()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)
