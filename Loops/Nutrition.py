def main():
    food = input('Item: ').lower().strip()
    drink = get_nutrition(food)
    print(drink)


def get_nutrition(n):
        fruits= {
                'apple':'Calories: 130',
                'avocado':'Calories: 50',
                'banana':'Calories: 110',
                'cantaloupe':'Calories: 50',
                'grapefruit':'Calories: 60',
                'grapes':'Calories: 90',
                'honeydew melon':'Calories: 50',
                'kiwifruit':'Calories: 90',
                'lemon':'Calories: 15',
                'lime':'Calories: 20',
                'nectarine':'Calories: 60',
                'orange':'Calories: 80',
                'peach':'Calories: 60',
                'pear':'Calories: 100',
                'pineapple':'Calories: 50',
                'plums':'Calories: 70',
                'strawberries':'Calories: 50',
                'sweet cherries':'Calories: 50',
                'tangerine':'Calories: 50',
                'watermelon':'Calories: 80',
                }
        for fruit in fruits:
              if fruit == n:
                   return fruits[fruit]

main()