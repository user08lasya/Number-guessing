import random 
number = random.randint(1, 100)

print("Welcome!")
print("Guess a number between 1 to 100")
print("I'll try to guess it")

attempts = 0
while True:
    attempts += 1
    guess = int(input("Enter you guessed number : "))

    if guess < number:
        print("It's too low!")
    elif guess > number:
        print("It's too high!")
    else:
        print("Congratulations! You guessed the number (number) in (attempts) attempts. ")
        break        