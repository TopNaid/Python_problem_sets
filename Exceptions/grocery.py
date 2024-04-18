counts = {}
while True:
    try:
        item = input('')
        item = item.upper()
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    except EOFError:
        break

sorted_items = sorted(counts.keys())
for item in sorted_items:
    print(f"{counts[item]} {item}")
