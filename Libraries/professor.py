import random


def main():
    score=0
    call = get_level()
    for _ in range(10):
        num1 = generate_integer(call)
        num2 = generate_integer(call)
        for _ in range(3):
            try:
                answer = int(input("{} + {} = ".format(num1, num2)))
                if answer == num1 + num2:
                    score +=1
                    break
                else:
                    print("EEE")
            except ValueError:
                pass
        else:
            print("{}".format(num1 + num2))
    else:
        print(f"Score: {score}")

def get_level():
    while True:
            try:
                level= int(input("Level: "))
                if level == 1 or level == 2 or level == 3:
                    return level

            except ValueError:
                pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
