import sys
import os
from tabulate import tabulate
import csv

if len(sys.argv) < 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

elif not os.path.isfile(sys.argv[1]):
    sys.exit("file does not exist")

com =[]
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for role in reader:
        com.append(role)
    print(tabulate(com, headers="keys", tablefmt="grid"))


