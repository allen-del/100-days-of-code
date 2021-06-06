#Rock Paper Scissors Game
import random
import sys
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

print("Welcome to Rock, Paper, Scissors!")
choice=int(input("Enter 0 for Rock, 1 for Paper and , 2 for Scissors :"))

if choice>2:
    sys.exit("Invalid choice!")


elif choice == 0:
    print(rock)

elif choice == 1:
    print(paper)

elif choice == 2:
    print(scissors)

computer_choice=random.randint(0,2)


print("Computer played :")

if computer_choice == 0:
    print(rock)

elif computer_choice == 1:
    print(paper)

elif computer_choice == 2:
    print(scissors)


if computer_choice==choice:
    print("Draw!")
elif computer_choice == 2 and choice==0:
    print("You Win!")

elif computer_choice>choice:
    print("Computer Wins!")



