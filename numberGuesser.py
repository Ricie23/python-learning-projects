import random

print("welcome to the number guessing game!")

while True:
    try:
        low = int(input("Enter the lowest number in the range: "))
        high = int(input("Enter the highest number in the range: "))
        if low >= high:
            print("The lowest number must be less than the highest number.")
            continue
        break
    except ValueError:
        print("Please enter valid integers.")

print(f"Guess a number between {low} and {high}.")

number = random.randint(low, high)
chances = 7
guessCounter = 0

while guessCounter < chances:
    try:
        guess = int(input("Enter your guess: ")) 
        guessCounter += 1

        if guess == number:
            print("Congratulations! You guessed the number!")
            break
        elif guess < number:
            print(f"Your guess is too low. {guessCounter} out of {chances} chances used.")
        elif guess > number:
            print(f"Your guess is too high. {guessCounter} out of {chances} chances used.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if guessCounter >= chances:
    print(f"Sorry, you've used all your chances. The number was {number}.")

