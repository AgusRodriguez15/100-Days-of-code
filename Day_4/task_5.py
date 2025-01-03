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
import random

list = [rock, paper, scissors]
computer_chose = random.choice(list)
player = int(input("Welcome to rock, paper or scissors choose one, type 0 for rock, 1 for paper and 2 for scissors\n"))
print(list[player])
print("computer chose")
print(computer_chose)
if list[player] == rock and computer_chose == scissors:
    print ("You win")
if list[player] == paper and computer_chose == rock:
    print ("You win")
if list[player] == scissors and computer_chose == paper:
    print ("You win")
if computer_chose == rock and list[player] == scissors:
    print ("You lost")
if computer_chose == paper and list[player] == rock:
    print ("You lost")
if computer_chose == scissors and list[player] == paper:
    print ("You lost")
if list[player] == computer_chose:
    print("you draw with the computer")