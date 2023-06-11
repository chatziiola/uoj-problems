import sys

n,m = [int(c) for c in input().split()]
field = 1

while n != 0 and m != 0:
    if field > 1:
        print()

    print(f"Field #{field}:")
    inputmatrix = [[''] * m for _ in range(n)]
    answermatrix = [[''] * m for _ in range(n)]

    # Handle input
    for li in range(n):
        line = input()
        for ch in range(m):
            inputmatrix[li][ch] = line[ch]
    
    for li in range(n):
        for ch in range(m):
            if inputmatrix[li][ch] == '*':
                answermatrix[li][ch] = '*'
                continue

            tmp = 0

            if ch > 0:
                if inputmatrix[li][ch-1] == '*':
                    tmp += 1
                if li > 0 and inputmatrix[li-1][ch-1] == '*':
                    tmp += 1
                if li < n-1 and inputmatrix[li+1][ch-1] == '*':
                    tmp += 1

            if ch < m-1:
                if inputmatrix[li][ch+1] == '*':
                    tmp += 1
                if li > 0 and inputmatrix[li-1][ch+1] == '*':
                    tmp += 1
                if li < n-1 and inputmatrix[li+1][ch+1] == '*':
                    tmp += 1

            if li > 0 and inputmatrix[li-1][ch] == '*':
                tmp += 1

            if li < n-1 and inputmatrix[li+1][ch] == '*':
                tmp += 1

            answermatrix[li][ch] = str(tmp)

    for line in range(n):
        for ch in range(m):
            print(answermatrix[line][ch],end='')
        print()
            
    field +=1 
    n,m = [int(c) for c in input().split()]




