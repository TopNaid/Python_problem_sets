from pyfiglet import Figlet
import sys
import random

def print_usage():
    print("Usage: python3 figlet.py (-f or--font & FONT_NAME) TEXT")
    sys.exit(1)

figlet = Figlet()
fonts = figlet.getFonts()
random_font = random.choice(fonts)

font_changer = Figlet()

if len(sys.argv) == 1:
    user_input = input("Input: ")
    font_changer.setFont(font=random_font)
    print(font_changer.renderText(user_input))
elif len(sys.argv) == 3:
    if sys.argv[1] in ['-f', '--font'] and sys.argv[2] in fonts:
        user_input = input("Input: ")
        font_changer.setFont(font=sys.argv[2])
        print(font_changer.renderText(user_input))
    else:
        print("Invalid font")
        print_usage()
else:  
    print("Invalid arguments")
    print_usage()