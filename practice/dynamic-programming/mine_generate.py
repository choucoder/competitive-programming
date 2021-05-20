from random import randint

def generate(n=15, m=15):
    for _ in range(n):
        row = [randint(5, 100) for _ in range(n)]
        print(" ".join(list(map(str, row))))

generate(20, 20)