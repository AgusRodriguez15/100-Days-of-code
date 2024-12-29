#PAUSE 2 - Check Odd or Even
#Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".
#
# Hint 
#1. First get the user input using the input() function.
#2. Next, convert the input into an int using the int() function.
#3. Now store the number in a variable.
#4. Use the modulo (%) to check if the user input number can be divided cleanly by 2.
#5. Use if/else to check if the result of the modulo check in step 4 is equal to 0 then that input number is even, otherwise it's odd.

number = int(input("insert a number:\n"))
type(number)
result = number % 2
if result == 0:
    print(number, "is even")
else:
    print(number, "is ood")