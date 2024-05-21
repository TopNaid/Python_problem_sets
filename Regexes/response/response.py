import validators


def main():
    user_input= input("What is your Email? ")
    to_valid = validate(user_input)
    print(to_valid)


def validate(s):
    email = validators.email(s)
    if email:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
