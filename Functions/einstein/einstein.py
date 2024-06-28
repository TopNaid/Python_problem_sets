def main():
    # user input
    mass = int(input("M: "))
    # call the function
    Est=check_mass(mass)
    print("E:",Est) 

# this is the function to convert mass to energy
def check_mass(mass):
    Est = mass *(300000000)**2
    return Est
main()

