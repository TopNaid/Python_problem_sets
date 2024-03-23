def convert(moji):
    moji = moji.replace(':)','🙂')
    moji = moji.replace(':(','🙁')
    return moji
def main():
    u_input = input(": ")
    convert_moji = convert(u_input)
    print(convert_moji)

main()
