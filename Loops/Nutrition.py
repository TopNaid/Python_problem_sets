def main():
    food = input('Item: ').lower().strip()
    drink = get_nutrition(food)
    print(drink)


def get_nutrition(n):
        if n == 'apple':
            return 'Calories: 130'
        elif n == 'avocado':
                return 'Calories: 50'
        elif n == 'banana':
                return 'Calories: 110'
        elif n == 'cantaloupe':
                return 'Calories: 50'
        elif n == 'grapefruit':
                return 'Calories: 60'
        elif n == 'grapes':
                return 'Calories: 90'
        elif n == 'honeydew melon':
                return 'Calories: 50'
        elif n == 'kiwifruit':
                return 'Calories: 90'
        elif n == 'lemon':
                return 'Calories: 15'
        elif n == 'lime':
                return 'Calories: 20'
        elif n == 'nectarine':
                return 'Calories: 60'
        elif n == 'orange':
                return 'Calories: 80'
        elif n == 'peach':
                return 'Calories: 60'
        elif n == 'pear':
                return 'Calories: 100'
        elif n == 'pineapple':
                return 'Calories: 50'
        elif n == 'plums':
                return 'Calories: 70'
        elif n == 'strawberries':
                return 'Calories: 50'
        elif n == 'sweet cherries':
                return 'Calories: 50'
        elif n == 'tangerine':
                return 'Calories: 50'
        elif n == 'watermelon':
                return 'Calories: 80'
        else: 
            return ''  
main()