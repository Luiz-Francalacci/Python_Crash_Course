from random import randint
class Dice:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        print(f"Result: {randint(1, self.sides)}")



dice = Dice()
print("6 sided die")
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
dice.roll_die()
print("10 sided die")
dice10 = Dice(10)
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
dice10.roll_die()
print("20 sided die")
dice20 = Dice(20)
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()
dice20.roll_die()