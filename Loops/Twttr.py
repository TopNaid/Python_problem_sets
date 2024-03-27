def main():
    soc = twitter()
    print(soc)

def twitter():
    twi = input('Input: ')
    result = ""
    vowels = "aeiouAEIOU"
    for char in twi:
        if char not in vowels:
            result += char
    return result
main()
            