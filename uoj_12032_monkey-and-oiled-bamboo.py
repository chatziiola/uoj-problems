cases = int(input())

for case in range(1, cases+1):
    try:
        numberOfSteps = int(input())
        # The zero here was added
        steps = [0] + [int(i) for i in input().split()]
    except EOFError:
        break
        
    currentK = 0
    # Solved in O(n), rather efficiently. No need to improve further, given input size. 
    for i in range(numberOfSteps, 0, -1):
        neededK = steps[i] - steps[i-1]
        if neededK == currentK:
            currentK += 1
        elif neededK > currentK:
            currentK = neededK

    print(f"Case {case}: {currentK}")
