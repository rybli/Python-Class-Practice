# Dice Rolling Program

# Original Problem Statement
# Write a program that will roll a 6-sided dice and display it with ascii art.

from random import randint


class Dice:
    # Die face count that are allowed.
    allowed_sides = [3, 4, 6, 8, 12, 20]

    def __init__(self, sides: int):
        """
        Create a die with a custom number of sides.
        :param sides: Number of sides for the die.
        """
        # Check if sides is valid.
        # Using most common face counts. (3, 4, 6, 8 , 12, 20)
        if sides not in self.allowed_sides:
            raise Exception("Please select a face value that is allowed.", self.allowed_sides)
        self.sides = sides

    def __repr__(self):
        return repr("A(n) %d-sided die" % self.sides)

    def roll(self, num_of_dice: int):
        """
        Roll a custom amount of dice.
        :param num_of_dice: Number of dice to roll.
        :return: List of values of dice rolled and sum of all rolls.
        """
        if num_of_dice <= 0:
            raise Exception("num_of_dice must be a positive int, got: ", num_of_dice)
        rolls = []
        for x in range(num_of_dice):
            rolls.append(randint(1, self.sides))

        return "Rolls: ", rolls,\
               "Total: ", sum(rolls)


def start():
    """
    Start the program and gather user input.
    Prints out list of rolls and total.
    Asks user if they want to re-roll.
    """
    dice_sides = int(input("What size die? "))
    number_of_dice = int(input("How many dice? "))
    d1 = Dice(dice_sides)

    print(d1.roll(number_of_dice), sep="\n")

    answer = input("Do you want to roll again? ")

    while answer == "y":
        print(d1.roll(number_of_dice))
        answer = input("Do you want to roll again? ")


if __name__ == "__main__":
    start()
    d2 = Dice(8)
    print(d2)
