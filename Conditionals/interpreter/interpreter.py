Expression = (input("Expression: "))

arith = Expression.split()
x = float(arith[0])
y = arith[1]
z = float(arith[2])

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "/":
    print(x / z)
elif y == "*":


    print(x * z)
else:
    print("Invalid")



