# dynamic
def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= count * coin
    return result


# greedy
def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0     
    used_coins = [-1] * (amount + 1)
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin
    result = {}
    while amount > 0:
        coin = used_coins[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    return result


# Main
if __name__ == '__main__':
    try:
        # dynamic
        amount = 113
        print(f"Dynamic programming for {amount}: {find_min_coins(amount)}")
        # greedy
        amount = 113
        print(f"A greedy algorithm for {amount}: {find_coins_greedy(amount)}")
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
