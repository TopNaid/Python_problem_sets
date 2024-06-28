"""This is a simple calculator.
    Inorder not to get an error whenever you run the program, let there
    be space between numbers and the operators. for example; 5 + 3,
    6 / 2, 20 * 3.
    Never do this 6/5, 8+6 or 7-2 etc
"""
def main():
    user_input= (input("Expression: "))
    y = get_operator(user_input)
    print(y ,end=" ")
   

def get_operator(n):
    arith = n.split()
    x = float(arith[0])
    y = arith[1]
    z = float(arith[2])

    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "/":
        return x / z
    elif y == "*":
        return x * z
    else:
        return "Invalid"

if __name__ == "__main__":
    main()


