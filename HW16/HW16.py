from random import randint


class Die(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


d = Die(6)
print(d.roll())
