# Rock, Paper, Scissors

import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

players_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if players_choice == 0:
    print(rock)
elif players_choice == 1:
    print(paper)
else:
    print(scissors)

computers_choice = random.randint(0, 2)
print("Computer chose:\n")
if computers_choice == 0:
    print(rock)
elif computers_choice == 1:
    print(paper)
else:
    print(scissors)

if players_choice == 0:
    if computers_choice == 0:
        print("It's a draw")
    elif computers_choice == 1:
        print("You lose")
    else:
        print("You win")
elif players_choice == 1:
    if computers_choice == 0:
        print("You win")
    elif computers_choice == 1:
        print("It's a draw")
    else:
        print("You lose")
else:
    if computers_choice == 0:
        print("You lose")
    elif computers_choice == 1:
        print("You win")
    else:
        print("It's a draw")
