#Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.
#Use the flow chart linked here to create the game logic.
#Once you've completed the project, you can always extend the game and make it more interesting!
# Hint 
#You can use the lower() function to turn any string into all lower case. https://www.w3schools.com/python/ref_string_lower.asp
#Alternatively you can also use the logical operator "or" to check for other spellings of user choice. e.g. Right, right or RIGHT.
import sys

print("Welcome to Treasure Island. Your mission is to find the treasure.")
print("Your mission is to find the treasure.")
print("Where do you want to go?")
print("Type left or right")
answer = input()
if answer != "left":
    print("Fall into a hole. Game Over.")
    sys.exit()
print("You've come to a lake. There is an island in the middle of the lake.")
print("'swim' to swim across or 'wait' to wait for a boat.")
answer2 =  input()
print(answer2)
if answer2 != "wait":
    print("Attacked by trout. Game Over")
    sys.exit()
print("You arrive at the island unharmed. There is a house with 3 doors.")
print("One red, One yellow and One blue. Which colour do you choose?")
asnwer3 = input()
if asnwer3 == "yellow":
    print("you win")
else:
    print("Game over.")
