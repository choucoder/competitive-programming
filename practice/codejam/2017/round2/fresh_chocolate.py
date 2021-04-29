import math

def solve(g, p):
    r = 0
    
    if p == 2:
        p0 = [gi for gi in g if (gi % p) == 0]
        p1 = [gi for gi in g if (gi % p) != 0]

        r = len(p0) + math.ceil(len(p1) / p)

    elif p == 3:
        p0 = [gi for gi in g if (gi % p) == 0]
        p1 = [gi for gi in g if ((gi + 1) % p) == 0]
        p2 = [gi for gi in g if ((gi + 2) % p) == 0]

        r = len(p0)

        while p1 and p2:
            p1.pop(0)
            p2.pop(0)
            r += 1
        
        if p1:
            r += math.ceil(len(p1) / p)
        if p2:
            r += math.ceil(len(p2) / p)

    else:
        p0 = [gi for gi in g if (gi % p) == 0]
        p1 = [gi for gi in g if ((gi + 1) % p) == 0]
        p2 = [gi for gi in g if ((gi + 2) % p) == 0]
        p3 = [gi for gi in g if ((gi + 3) % p) == 0]

        r+= len(p0)

        while p1 and p3:
            p1.pop(0)
            p2.pop(0)
            r += 1
        
        while len(p2) > 1:
            r += 1
            p2.pop(0)
            p2.pop(0)
        
        if p3:
            if len(p3) < 2 or len(p2) < 2:
                r += 1
            elif len(p3) == 2 or len(p2) == 2:
                r += 1
            else:
                p3.pop(0)
                p3.pop(0)
                p2.pop(0)
                r += math.ceil(len(p3) / 3) + 1
        
        if p1:
            if len(p1) < 2 or len(p2) < 2:
                r += 1
            elif len(p1) == 2 or len(p2) == 2:
                r += 1
            else:
                p1.pop(0)
                p1.pop(0)
                p2.pop(0)
                r += math.ceil(len(p1) / 3) + 1

    return r
        

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t + 1):
        n, p = [int(i) for i in input().split()]
        g = [int(i) for i in input().split()]
        print(f"Case: #{case}: {solve(g, p)}")