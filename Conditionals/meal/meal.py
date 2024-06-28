def main():
    time = input("What time is it: ").strip()
    if convert(time) >= 7 and convert(time) <= 8:
        print("Breakfast time")
    elif convert(time) >= 12 and convert(time) <= 13:
        print("Lunch time")
    elif convert(time) >= 18 and convert(time) <= 19:
        print ("Dinner time")
    else:
        print(" ")

def convert(n):
    split= n.split(":")
    hours = int(split[0])
    minute = int(split[1])

    day = hours + ( minute / 60)
    return day


if __name__ == "__main__":
    main()


  