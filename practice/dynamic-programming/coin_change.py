def minChange(money, coins, dp={}):
    if money in dp: return dp[money]
    if money == 0: return []
    if money < 0: return None

    minCoins = None

    for c in coins:
        remainder = money - c
        remainderCoins = minChange(remainder, coins)
        if remainderCoins != None:
            _coins = remainderCoins + [c]
            if (minCoins == None or len(_coins) < len(minCoins)):
                minCoins = _coins
    
    dp[money] = minCoins
    return minCoins


if __name__ == '__main__':
    n = 8
    c = [2, 5, 3]
    print(len(minChange(n, c)))