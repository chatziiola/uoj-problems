from queue import deque

cases = 1+ int(input())

for case in range(1,cases):
    even = 0
    odd = 0

    # R: rows
    # C: columns
    # M: movesVertically
    # N: movesHorizontally 
    r,c,m,n = [int(i) for i in input().split()]

    # W: number of water locations
    w = int(input())

    grid = [[-1]*c for row in range(r)]

    # Water locations
    for i in range(w):
        a,b = [int(i) for i in input().split()]
        grid[a][b] = -2 # water code
        
    # Different checks: keeping (r,c)
    checks = [(+m,+n),(+m,-n),(-m,+n),(-m,-n),(+n,+m),(+n,-m),(-n,+m),(-n,-m)]
    myQ = deque()
    myQ.append((0,0))
    grid[0][0] += 1

    # There's an edge case I'm missing with the 1 0
    while len(myQ) > 0:
        # currSq[0] = row
        # currSq[1] = col
        currentSquare = myQ.popleft()

        checkedSquares = set()
        for l in range(8):
            tmpRow = (currentSquare[0] + checks[l][0])
            tmpCol = (currentSquare[1] + checks[l][1])
            if (tmpRow,tmpCol) in checkedSquares:
                continue
            checkedSquares.add((tmpRow,tmpCol))
            if ((tmpRow > -1) and (tmpRow < r)) and\
               ((tmpCol > -1) and (tmpCol < c)) and\
               grid[tmpRow][tmpCol] != -2:
                grid[tmpRow][tmpCol] += 1
                # This is the visited condition: -1 unvisited, and since it was just incremented: +1
                if grid[tmpRow][tmpCol] == 0:
                    myQ.append((tmpRow, tmpCol))

    
    grid[0][0] -= 1
    for row in range(r):
        for col in range(c):
            if grid[row][col] > -1:
                if grid[row][col] % 2 == 0:
                    odd += 1
                else:
                    even +=1

    # My way even though might be more memory efficient than any else
    # I've seen, does not really take into consideration the case
    # where we can only "stay" on the first block
    if even == odd and even == 0:
        even += 1
   
    print(f"Case {case}: {even} {odd}")
