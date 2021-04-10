from pprint import pprint

def solve(deck, n):
    max_score = 0

    for i in range(n):
        for j in range(i, n):
            prod = deck[i] * deck[j]
            print(f"{deck[i]} * {deck[j]}")
            _sum = 0

            for k in range(n):
                if k != i and k != j:
                    _sum += deck[k]
            print(f"score: {max_score}, {_sum} == {prod}")
            if _sum == prod:
                max_score = prod

    return max_score

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t + 1):
        m = int(input())
        deck = []

        for _ in range(m):
            pn = input().split()
            p = int(pn[0])
            n = int(pn[1])
            for _ in range(n):
                deck.append(p)
        print(f"Mazo: {deck}")
        print(f"Case #{case}: {solve(deck, len(deck))}")