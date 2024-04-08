total = 0
taq = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
while True:
    try:
        item = input('Item: ').title().strip()
        price = taq.get(item)
        if price is None:
            continue
        elif price is not None:
             total += price
             print(f'Total: ${"{:.2f}".format(total)}')
    except EOFError:
         break
        
