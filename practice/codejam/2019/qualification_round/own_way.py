def solve(n=2, p='SE'):
    _p = ''
    _aux = ''
    for pi in p:
        _aux += pi
        if _aux.count('E') and _aux.count('S'):
            _aux = _aux[::-1]
            _p += _aux
            _aux = ''
    return _p


if __name__ == '__main__':
    
    T = int( input() )

    for case in range(1, T + 1):
        N = int( input() )
        P = input()
        print("Case #{}: {}".format(case, solve(N, P)))