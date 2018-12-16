import random

number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print("what is " + str(number1) + " + " + str(number2) + "?")
# answer = input()
answer = int(input())
if answer == number1 + number2:  # by comparing string and int, it's never going to be equal.
    print("Correct!")
else:
    print("Nope! The answer is " + str(number1 + number2))
