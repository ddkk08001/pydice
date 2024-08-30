import os
import random
os.system("clear")

# Posible Outputs
roll1 = """
ooooooooooooo
o           o
o           o
o     #     o
o           o
o           o
ooooooooooooo
"""

roll2 = """
ooooooooooooo
o           o
o   #       o
o           o
o       #   o
o           o
ooooooooooooo
"""

roll3 = """
ooooooooooooo
o           o
o   #       o
o     #     o
o       #   o
o           o
ooooooooooooo
"""

roll4 = """
ooooooooooooo
o           o
o   #   #   o
o           o
o   #   #   o
o           o
ooooooooooooo
"""

roll5 = """ 
ooooooooooooo
o           o
o   #   #   o
o     #     o
o   #   #   o
o           o
ooooooooooooo
"""

roll6 = """
ooooooooooooo
o           o
o   #   #   o
o   #   #   o
o   #   #   o
o           o
ooooooooooooo
"""

while True:
    input("Press Enter to roll the dice and press Ctrl+C to exit.")

    os.system("clear")

    # Random Number
    dice = random.randint(1,6)

    print("You rolled a", dice)

    # Output
    if dice == 1:
        print(roll1)
    elif dice == 2:
        print(roll2)
    elif dice == 3:
        print(roll3)
    elif dice == 4:
        print(roll4)
    elif dice == 5:
        print(roll5)
    else:
        print(roll6)
