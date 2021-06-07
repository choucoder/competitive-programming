from typing import List


def bigIntegerSum(a: List[int], b: List[int]) -> List[int]:
    a = a[::-1]
    b = b[::-1]

    result = []
    remainder = 0

    while a and b:
        c = a.pop(0) + b.pop(0) + remainder
        result.insert(0, c % 10)
        remainder = c // 10

    remainder_list = a if a else b

    while remainder or remainder_list:
        if remainder_list:
            c = remainder_list.pop(0) + remainder
        else:
            c = remainder
        result.insert(0, c % 10)
        remainder = c // 10
        
    return result


def bigIntegerMult(a: List[int], b: List[int]):
    """Multily a * b (grade-school algorithm).
    """
    res = []

    for i, bi in enumerate(b[::-1]):
        remainder = 0
        mult = [0 for _ in range(i)]
        
        for ai in a[::-1]:
            prod = ai * bi
            result = prod + remainder
        
            remainder = result // 10
            mult.insert(0, result % 10)

        if remainder:
            mult.insert(0, remainder % 10)

        if not res:
            res = mult[:]
        else:
            res = bigIntegerSum(res, mult[:])

    return ''.join(list(map(str, res)))


if __name__ == '__main__':

    # n1 = "3141592653589793238462643383279502884197169399375105820974944592"
    # n2 = "2718281828459045235360287471352662497757247093699959574966967627"
    for n1 in range(10**9):
        for n2 in range(10*4):
            n1, n2 = str(n1), str(n2)
            a = [int(ni) for ni in n1]
            b = [int(ni) for ni in n2]

            res = int(bigIntegerMult(a, b))
            hardcode_res = int(n1) * int(n2)
            # print(f"Case #1: {res} : {int(n1)*int(n2)}. {int(res) == int(n1)*int(n2)}")
            print(res == hardcode_res, res, hardcode_res, n1, n2)