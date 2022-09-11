def main():
    dict = {}
    get_list(dict)
    for item in sorted(dict):
        print(dict[item], item)

def get_list(dict):
    while True:
        try:
            item = input().upper()
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
        except EOFError:
            print()
            break
main()