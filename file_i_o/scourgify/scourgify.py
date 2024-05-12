import sys
import os
import csv

def main():
    command_line()


    try:
        names = []

        with open(sys.argv[1], newline='') as infile:
            reader = csv.DictReader(infile)
        
            for row in reader:
                namer= row['name'].split(",")
                names.append({"first": namer[1].lstrip(), "last": namer[0].lstrip(), "house":row['house']})

        with open(sys.argv[2], "w", newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in names:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

def command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif not os.path.isfile(sys.argv[1]):
        sys.exit("Not a csv file")


if __name__ == "__main__":
    main()
