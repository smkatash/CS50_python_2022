def main():
    print("Amount Due: 50")
    amount = 50
    get_status(amount)

def get_status(amount):
    while True:
        coin = int(input("Insert Coin: "))
        if coin not in [5, 10, 25]:
            print("Amount Due: 50")
            break
        else:
            amount = get_update(coin, amount)
            if amount <= 0:
                break

def get_update(coin, amount):
    if amount:
        amount = amount - coin
        if amount == 0:
            print("Change owed: ", amount)
        elif amount < 0:
            print("Change owed: ", amount * -1)
        else:
            print("Amount Due: ", amount)
    return amount

main()