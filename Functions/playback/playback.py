def main():
    # get user input
    # use the split method to split user input
    user_input = input(": ").split()
    # call the get_dots function defined below and store the result in the dots variable
    dots= get_dot(user_input)
    print(dots)

def get_dot(cold):
    # use join method to join user input with dots in between
    world_dots ="...".join(cold)
    return world_dots
main()
