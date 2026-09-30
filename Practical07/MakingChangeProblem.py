coins = list(map(int, input("Enter coin values: ").split()))
amount = int(input("Enter amount: "))

coins.sort(reverse=True)
count = 0

for coin in coins:
    n = amount // coin
    if n > 0:
        print(coin, "x", n)
        count += n
        amount %= coin

print("Minimum coins:", count)
