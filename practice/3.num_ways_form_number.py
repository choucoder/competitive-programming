"""
Given 3 numbers {1, 3, 5}, we need to tell the total
number of ways we can form a number 'N' using the sum
of the given three numbers.
"""
def solve_verbose(arr, n, total):
    ways = 0

    if sum(total) == n:
        print(total)
        return 1
    elif sum(total) > n:
        return 0
    else:
        for i in arr:
            total.append(i)
            ways += solve_verbose(arr, n, total)
            if total:
                total.pop()
        return ways


def solve(arr, n, total):
    ways = 0

    if total == n:
        return 1
    elif total > n:
        return 0
    else:
        for i in arr:
            total += i
            ways += solve(arr, n, total)
            total -= i
        
        return ways

if __name__ == '__main__':
    arr = [1, 3, 5]
    n = 6
    r = solve_verbose(arr, n, [])
    print(f"Case #1: {r}")
    r = solve(arr, n, 0)
    print(f"Case #2: {r}")