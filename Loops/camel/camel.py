def main():

    camel = input("camelCase: ")
    animal = camel2snake(camel)
    print(f"snake_case: {animal}")

def camel2snake(camel):
    snake = []
    for char in camel[:]:
        if char.isupper():
            snake.append('_')
        snake.append(char.lower())
    return ''.join(snake)

main()