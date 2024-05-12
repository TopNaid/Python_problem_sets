import sys
import os

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")
elif len(sys.argv) < 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not os.path.isfile(sys.argv[1]):
    sys.exit("file does not exist")

counter = 0
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith('#'):
            counter += 1
    print(counter)


