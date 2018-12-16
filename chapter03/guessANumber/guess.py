import random

guessTaken = 0

print("hello, what's your name?")
name = input("> ")

number = random.randint(1, 20)

print("well, " + name + ", I thought of a number between 1 and 20. can you guess it?")

for guessTaken in range(6):
    print("take a guess")
    guess = input("> ")
    guess = int(guess)

    if guess < number:
        print("your number is to low")

    if guess > number:
        print("your number is too high")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessTaken + 1)
    print("good job, " + name + ", you guessed the number " + str(number) + " in " + guessesTaken + " guesses")

if guess != number:
    print("unlucky. you did not make it to the end. the number I thought of was " + str(number))


