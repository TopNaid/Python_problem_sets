
import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        if not name:  # If an empty line is entered
            break
        names.append(name)
    except EOFError:
        break

count = len(names)
if count == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif count == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
else:
    farewell = ', '.join(names[:-1]) + ', and ' + names[-1]
    print(f"Adieu, adieu, to {farewell}")

