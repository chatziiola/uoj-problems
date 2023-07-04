cases = int(input())

while cases:
    try:
        inputarray = [int(i) for i in input().split()]
    except EOFError:
        break

    # Number of relatives
    r = inputarray[0]
    inputarray.pop(0)

    activeStreets = set([])
    streetCosts = [0]*30001

    # This works in O(n)
    for i in inputarray:
        streetCosts[i] += 1
        activeStreets.add(i)


    minSum = float('inf')

    # The optimal solution will necessarily be for vito to stay on a street with relatives.
    # O(n^2) algorithm, could this be improved? I dont think so 
    # O(n) outer loop
    for street in activeStreets:
        tmpSum = 0
        # O(n) inner loop
        for otherStreet in activeStreets-set([street]):
            tmpSum += streetCosts[otherStreet]*(abs(otherStreet-street))
        minSum  = min(tmpSum, minSum)


    print(f"{minSum}")
        
    
    
