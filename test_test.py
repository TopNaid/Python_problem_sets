import sys
import os
from PIL import Image,ImageOps

try:
    desired_size = (450, 450)  # Example size: (width, height)

    muppet =Image.open(sys.argv[2])
    size = muppet.size
    muppet=ImageOps.fit(muppet,desired_size)


    shirt = Image.open(sys.argv[1])
    shirt = shirt.resize(desired_size)
    muppet.paste(shirt, (0, 0))
    muppet.save("Output.png")

except FileNotFoundError:
    sys.exit("File Not Found")

   try:
        desired_size = (450, 450)  # Example size: (width, height)

        muppet =Image.open(sys.argv[2])
        size = muppet.size
        muppet=ImageOps.fit(muppet,desired_size)

        shirt = Image.open(sys.argv[1])
        shirt = shirt.resize(desired_size)
        muppet.paste(shirt, (0, 0))
        muppet.save("Output.png")

    except FileNotFoundError:
         sys.exit("File Not Found")