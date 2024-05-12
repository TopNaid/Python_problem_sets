import sys
import os
from PIL import Image,ImageOps


def main():
    command_line()

    try:
        desired_size = (600, 500)  # Example size: (width, height)
        muppet = Image.open(sys.argv[1])
        muppet = ImageOps.fit(muppet, desired_size)

        shirt = Image.open('shirt.png')
        size = shirt.size
        muppet.paste(shirt, shirt)
        muppet.save(sys.argv[2])



#background_image.paste(overlay_image, (upper_left_x, upper_left_y))

    except FileNotFoundError:
        sys.exit("File Not Found")

def command_line():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    _, ext1 = os.path.splitext(sys.argv[1])
    _, ext2 = os.path.splitext(sys.argv[2])
    if ext1.lower() not in ['.jpg', '.jpeg', '.png'] or ext2.lower() not in ['.jpg', '.jpeg', '.png']:
        sys.exit("Not a jpg, jpeg, or png file")

    elif ext1 != ext2:
        sys.exit("Input and output have different extensions")

    elif not os.path.exists(sys.argv[1]):
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()

