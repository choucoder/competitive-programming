import math

def getPrimesFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    i = 3
    while i <= int(math.sqrt(n)):
        while ( n % i == 0 ):
            factors.append(i)
            n = n / i
        i += 1

    if (n > 2):
        factors.append(int(n))
    
    print(factors)

if __name__ == '__main__':
    n = 30
    getPrimesFactors(n)