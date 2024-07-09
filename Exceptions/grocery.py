def main():
    counts = {}
    
    while True:
        try:
            item = input('').strip().lower()
            if item:
                get_grocery(item, counts)
        except EOFError:
            break

    sorted_items = sorted(counts.keys())
    for item in sorted_items:
        print(f"{counts[item]} {item.upper()}")


def get_grocery(item, counts):
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1


main()

