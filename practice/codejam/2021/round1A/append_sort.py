def solve(x, n):

    r = 0

    for i in range(1, n):
        _min = x[i - 1]
        s = len(str(_min)) - 1
        xi = int(str(x[i]) + '0'*s)

        if xi < _min:
            xi = int(str(xi) + '0')
            s = s + 1
        
        limit = (10**s)
        for j in range(0, limit):
            if xi < _min:
                xi = xi + j
        
        x[i] = xi
        r += s

    return r


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        x = [int(s) for s in input().split()]
        print(f"Case #{case}: {solve(x, len(x))}")