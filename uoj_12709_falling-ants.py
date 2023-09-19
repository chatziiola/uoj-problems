# Input routine seems ok

n = int(input())


# It is given in the problem definition that f = g - g/2h => f = g ( 1
# - 1/2h), which translates that, the higher the H the higher the
# value of f.

# In case of a tie, the biggest volume is asked.

# Solution:
# 1. Sort based on h (one could also just store based on h - no need to keep everything) - we want hmin
# 2. 

while n != 0:
    # print(f"Ants: {n}")
    hMax = 0
    antArr = []
    for i in range(n):
        l,w,h = [int(i) for i in input().split()]
        if hMax < h:
            hMax = h
            antArr.clear()

        if hMax == h:
            antArr.append(l*w*h)
            
            
    antArr.sort()
    # print(antArr)
    print(antArr[-1])
    n = int(input())
