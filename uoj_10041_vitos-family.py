cases = int(input())

while cases:
    try:
        inputarray = [int(i) for i in input().split()]
    except EOFError:
        break

    # Number of relatives
    r = inputarray[0]
    inputarray.pop(0)

    inputarray.sort()

    median = inputarray[r//2]

    misum = 0
    for i in range(r):
        misum += abs(inputarray[i] - median)

    print(misum)
        
        
    
    
