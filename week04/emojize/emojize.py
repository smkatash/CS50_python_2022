import emoji

def main():
    str = input("Input: ").strip()
    print(emoji.emojize('Output: {}'.format(str), language='alias'))


main()