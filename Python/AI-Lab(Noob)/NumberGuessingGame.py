import random as rnd 

def guessNum():

    randomNum = rnd.randint(1, 100)
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == randomNum:
                print("Congratulations! You guessed the number correctly.")
                break
            elif guess > randomNum:
                print("Too high! Try again.")
            else:
                print("Too low! Try again.")
        except ValueError:
            print("Please enter a valid integer.")
    


if __name__ == "__main__":
    guessNum()
