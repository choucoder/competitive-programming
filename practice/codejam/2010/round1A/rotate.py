def printBoard(b):
    for row in b:
        print(row)


def solve(b, n, k):
    rb = []
    result = ""
    red, blue = False, False

    # First step rotate 90 degrees
    j = 0
    while j < n:
        i = n - 1
        row = []
        while i >= 0:
            row.append(b[i][j])
            i -= 1
        rb.append(row)
        j += 1

    # Second step apply gravity
    for j in range(n):
        i = n - 1
        while i >= 0:
            if rb[i][j] == '.':
                l = max(0, i - 1)
                m = i
                while rb[l][j] == '.' and l > 0:
                    l -= 1
                    if l < 0:
                        break
                while l >= 0 and rb[l][j] != '.':
                    rb[m][j], rb[l][j] = rb[l][j], rb[m][j]
                    l = l - 1
                    m = m - 1
            i -= 1

    # Thirty step
    ## Rows count
    for i in range(n):
        row = ''.join(rb[i])
        if row.count('R'*k) >= 1:
            red = True
        if row.count('B'*k) >= 1:
            blue = True
        
    ## Cols count
    for j in range(n):
        col = ''
        for i in range(n):
            col += rb[i][j]
        if col.count('R'*k) >= 1:
            red = True
        if col.count('B'*k) >= 1:
            blue = True
    
    ## Diagonal principal
    dp = [rb[i][i] for i in range(n)]
    
    dp = ''.join(dp)
    if dp.count('R'*k) >= 1:
        red = True
    if dp.count('B'*k) >= 1:
        blue = True

    # Diagonal principal arriba
    idp = [[i, i] for i in range(n)]
    for col in range(n - 1):
        idp = [[i, j + 1] for i, j in idp]
        idp = [coord for coord in idp if coord[1] < n]
        sdp = ''
        for i, j in idp:
            sdp += rb[i][j]
        if sdp.count('R'*k) >= 1:
            red = True
        if sdp.count('B'*k) >= 1:
            blue = True

    #Diagonal principal abajo
    idp = [[i, i] for i in range(n)]
    for row in range(n - 1):
        idp = [[i + 1, j] for i, j in idp]
        idp = [coord for coord in idp if coord[0] < n]
        sdp = ''
        for i, j in idp:
            sdp += rb[i][j]
        if sdp.count('R'*k) >= 1:
            red = True
        if sdp.count('B'*k) >= 1:
            blue = True

    # Diagonal secundaria
    idp = []
    i = 0
    j = n - 1
    while j >= 0 and i < n:
        idp.append([i, j])
        j = j - 1
        i = i + 1
    ds = ''.join([rb[i][j] for i, j in idp])
    if ds.count('R'*k) >= 1:
        red = True
    if ds.count('B'*k) >= 1:
        blue = True
    
    idp2 = idp[::]
    
    # Diagonal secundaria arriba
    for col in range(n):
        idp = [[i, j - 1] for i, j in idp]
        idp = [coord for coord in idp if coord[1] >= 0]
        sdp = ''
        for i, j in idp:
            sdp += rb[i][j]
        if sdp.count('R'*k) >= 1:
            red = True
        if sdp.count('B'*k) >= 1:
            blue = True
    
    # Diagonal secundaria abajo
    idp = idp2[::]
    for col in range(n):
        idp = [[i + 1, j] for i, j in idp]
        idp = [coord for coord in idp if coord[0] < n]
        sdp = ''
        for i, j in idp:
            sdp += rb[i][j]
        if sdp.count('R'*k) >= 1:
            red = True
        if sdp.count('B'*k) >= 1:
            blue = True
    
    if red and blue:
        result = "Both"
    elif red and not blue:
        result = "Red"
    elif not red and blue:
        result = "Blue"
    else:
        result = "Neither"
    
    return result


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t + 1):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        b = [[s for s in input()] for _ in range(n)]
        print(f"Case #{case}: {solve(b, n, k)}")