def main():
    word = input("Input: ")
    soc = shorten(word)
    print(soc)

def shorten(word):
    result = ""
    vowels = "aeiouAEIOU"
    for char in word:
        if char not in vowels:
            result += char
    return result

if __name__=="__main__":
    main()
            

