def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(soup):
    if len(soup) < 2:
        return False
    if (soup[0].isalpha() and soup[1].isalpha()) and (2 <= len(soup) <= 6):
            if not soup.isalnum():
                return False
            num_started = False
            for char in soup[2:]:
                if char.isdigit():
                    if char == '0' and not num_started:
                        return False
                    num_started = True
                elif num_started:
                    return False
            else:
                return True

    else:
        return False


if __name__ == "__main__":
    main()











