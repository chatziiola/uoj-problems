# Seems pretty easy
# Got wrong answer tho

N = int(input())

cases = 2

while N:
    startingLineUp = [0]*(N+1)
    impossibol = False
    for position in range(1,N+1):
        C,P = [int(i) for i in input().split()]
        supposedStartingPos = position + P
        if supposedStartingPos > N \
           or supposedStartingPos < 0\
           or startingLineUp[supposedStartingPos]:
            impossibol = True # possibol :P
            continue
            # break  - can't break need to see all of the input
        startingLineUp[supposedStartingPos] = C

    if impossibol:
        print("-1")
    else:
        for car in range(1,N):
            print(f"{startingLineUp[car]} ")
        print(f"{startingLineUp[-1]}")

    N = int(input())
