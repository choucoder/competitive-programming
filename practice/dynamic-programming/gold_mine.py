def solve(mine, r, c, n, m, dp={}):
    if f'{r},{c}' in dp: return dp[f'{r},{c}']

    if r < 0 or r >= n:
        return 0
    elif c == (m - 1):
        return mine[r][c]
    else:
        result = max(solve(mine, r - 1, c + 1, n, m, dp=dp), solve(mine, r, c + 1, n, m, dp=dp), solve(mine, r + 1, c + 1, n, m, dp=dp))
        result = result + mine[r][c]
        dp[f'{r},{c}'] = result
        return result


def initialize(mine, n, m):
    dp = {}
    maxGold = 0
    for i in range(n):
        maxGold = max(solve(mine, i, 0, n, m, dp=dp), maxGold)
    return maxGold


if __name__ == '__main__':
    cases = int(input())

    for case in range(1, cases + 1):
        n, m = [int(n) for n in input().split()]
        mine = []
        for i in range(m):
            mine.append(list(map(int, input().split())))
        print(f"Case #{case}: {initialize(mine, n, m)}")