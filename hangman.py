import random
from collections import Counter

randomWords = '''apple cherry banana 
radio water foot backball table 
chair computer phone television'''

randomWords = randomWords.split()
word = random.choice(randomWords)
if __name__ == '__main__':
    print("Welcome to the Hangman game!")
    for i in word:
        print("_", end=" ")
    print()

    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while(chances != 0) and flag == 0:
            print()
            chances -= 1

            try:
                guess = input("Guess a letter: ").lower()
            except ValueError:
                print("Invalid input. Please enter a single letter.")
                continue

            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single Letter.")
                continue
            elif guess in letterGuessed:
                print("You have already guessed that letter.")
                continue
        
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess
            
            for char in word:
                if char in letterGuessed:
                    print(char, end=" ")
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)):
                    print('the word is:', end=" ")
                    print(word)
                    flag = 1
                    print("You have won the game!")
                    break
                    break
                else:
                    print("_", end=" ")

        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print("You have lost the game!")
            print("The word was:", word)
    
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
        exit()



