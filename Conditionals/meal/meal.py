# def main():

#     time_input =input("What time is it: ")
#     meal= time_input.split(":")
#     hour = float(meal[0])
#     minute = float(meal[1])
#     meal_time = convert(hour)
#     print(meal_time)  

# def convert(time):
#     if time >= 7 and time < 8:
#         return "Breakfast time"
#     elif time >= 12 and time < 13:
#         return "Lunch time"
#     elif time >= 18 and time < 19:
#         return "Dinner time"
#     else:
#         return " "

# if __name__ == "__main__":
#     main()

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


def convert(time):
    split= time.split(":")
    hours = int(split[0])
    minute = int(split[1])

    day = hours + ( minute / 60)
    return day


if __name__ == "__main__":
    main()




# def main():
#     time = input("What time is it: ").strip()
#     if convert(time) >= 7 and convert(time) <= 8:
#         print("Breakfast time")
#     elif convert(time) >= 12 and convert(time) <= 13:
#         print("Lunch time")
#     elif convert(time) >= 18 and convert(time) <= 19:
#         print ("Dinner time")
#     else:
#         print(" ")


# def convert(time):
#     hours, minute = time.split(":")
#     return float(hours) + float(minute) / 60
    


# if __name__ == "__main__":
#     main()


  