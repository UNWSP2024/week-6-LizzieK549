
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    # Sum 2 numbers
    sum2 = roll1 + roll2
    # return sum to calling function
    return sum2

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main():
    total = 0
    rolls = 100

    for n in range(rolls):
        total += randDice()

    average = total/rolls
    print("Average of 100 rolls is "f"{average:,.2f}")

main()


