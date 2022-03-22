import random


dice_size = int(input("Dice number of sides: "))


decay_number = int(input("Decay when this number or less is rolled: "))

dice_number = int(input("Number of dice to roll: "))

print("To escape from the sim, type 'q'")

current_number = dice_number
total_decayed = 0
iteration_number = 0

while True:
    current_decays = 0
    iteration_number += 1
    for i in range(current_number):
        if random.randint(1,dice_size) <= decay_number:
            current_decays += 1
            total_decayed += 1
            current_number -= 1
    print(" "*(7-len(str(iteration_number))),iteration_number, ": Decays: ", current_decays, " "*(7-len(str(current_decays))), " Remaining: ", current_number, " "*(7-len(str(current_number))), "   Total decays: ", total_decayed, end='')
    if input() == 'q':  
        break

