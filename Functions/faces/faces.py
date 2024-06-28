def main():
    u_input = input(": ")
    convert_moji = convert(u_input)
    print(convert_moji)

def convert(moji):
    # when user input :), they should get a smiley face
    # when user input :(, they should get an angry face
    moji = moji.replace(':)','🙂')
    moji = moji.replace(':(','🙁')
    return moji
main()
