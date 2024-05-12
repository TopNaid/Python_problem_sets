names =[]

for _ in range(3):
    name = input("what is your name? ")
    names.append(name)
for name in sorted(names):
    print(name)
