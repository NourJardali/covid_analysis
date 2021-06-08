import random

x = random.randint(0, 100)
count = 0
guess = int(input("Can you guess the number? "))
while guess != x:
    count += 1
    if guess > x:
        guess = int(input("Your guess is high. Try again: "))
    else:
        guess = int(input("Your guess is low. Try again: "))

if guess == x:
    count += 1
    print("Congratulations. You guessed the number with ",count," guesses")