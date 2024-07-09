def main():
    filling = get_fuel()
    print (filling)

def get_fuel():  
    while True:  
        try:
            fuel = input('Fraction: ')
            can = fuel.split('/')
            x = int(can[0])
            y = int(can[1])
            if x > y:
                continue
            cat = round(x/y * 100) 
            if cat >= 99:
                return 'F' 
            elif cat <= 1:
               return 'E'
        except (ValueError,ZeroDivisionError, IndexError):
                pass
       
        else:
            return f'{cat}%'
        
main()

        
        
