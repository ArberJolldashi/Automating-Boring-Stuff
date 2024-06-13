# This is a guess the number game.
import random

print('Hello, what is your name?')
name = input()

print(f"Well, {name} I am thinking of a number between 1 and 20 ")

secret_number = random.randint(1, 20)
print('Please input a number')

for guesses_taken in range(1, 7):
    print('Take a guess.')
    try:
        guess = int(input())
    except ValueError, NameError:
        print('Please input numbers only')
        
    if guess < secret_number:
        print('Your guess is to low.')
    elif guess > secret_number:
        print('Your guess is to high.')
    else:
        break # guess == secret_number


if guess == secret_number:
    print(f'Good job {name}, you guessed my number with {guesses_taken} guesses')
else:
    print(f'Nope, The number that I was thinking of was {secret_number}')
