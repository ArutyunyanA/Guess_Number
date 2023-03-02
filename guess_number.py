
import random

def guessNumber():

        guessTaken = 0
        print('Hello! Welcome to game guess number, what is your name?')
        myName = input()
        number = random.randint(1, 20)
        print(f'Well,{myName}, I am thinking of number between 1 and 20.')

        for guessTaken in range(6):
                print('Take a guess.')
                guess = input()
                guess = int(guess)

                if guess < number:
                        print('Your guess is too low, keep trying.')

                if guess > number:
                        print('Your guess is too high, keep trying.')

                if guess == number:
                        break

        if guess == number:
                guessTaken == str(guessTaken + 1)
                print(f'Good job, {myName}! You guessed my number in  {guessTaken}  guesses!')

        if guess != number:
                number = str(number)
                print(f'Nope. The number I was thinking of was {number}.')


if __name__ == '__main__':
        guessNumber()
