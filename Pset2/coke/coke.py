def main():

    due = 50

    while due > 0:
        print(f"Amount Due: {due}")
        coin = input("Insert Coin: ")

        if coin in ("5", "10", "25"):
            due -= int(coin)

        if due <= 0:
            print(f"Change Owed: {due * -1}")

main()
