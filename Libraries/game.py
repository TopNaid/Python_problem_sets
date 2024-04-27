import random
import sys

def main():
    while True:
        try:
            user_input= int(input("Level: "))
            ran = random.randint(1, user_input)
            while True:
                cat = get_guess()
                if cat < ran:
                    print("Too small!")
                elif cat > ran:
                    print("Too large!")
                else:
                    sys.exit("Just right!")

        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            return guess
        except ValueError:
            pass
main()
