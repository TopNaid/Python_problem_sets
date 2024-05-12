def main():
    fuel = input('Fraction: ')
    percentage = convert(fuel)
    category = gauge(percentage) 
    print(category)
    

def convert(fraction):
    while True:
        try: 
            fact = fraction.split('/')
            x = int(fact[0])
            y = int(fact[1])
            if x > y: 
                raise TypeError("The numerator cannot be greater than the denominator.")
    
            p = round(x/y * 100)
            return p
        except(ValueError,ZeroDivisionError):
            pass
                      
def gauge(percentage):
        
        if percentage >= 99:
            return 'F' 
        elif percentage <= 1:
            return 'E'

        else:
             return f'{percentage}%'
    
if __name__ == "__main__":
    main()




