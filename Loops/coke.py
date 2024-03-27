def main():
    coke_machine()

def coke_machine():
    print("Amount Due: 50")
    total_inserted = 0
    amount_due = 50

    while total_inserted < amount_due:
        amount_insert = int(input("Insert Coin: "))

        if amount_insert not in [25, 10, 5]:
            print(f"Amount Due: {amount_due}")
            continue

        total_inserted += amount_insert
        remaining_due = amount_due - total_inserted
        if remaining_due >= 0 :
            print(f"Amount Due: {remaining_due}")

    change_due = total_inserted - amount_due
    print(f"Change Owed: {change_due}")

main()



 