# For each case
while True:
    # Handle input
    while True:
        sequence = []
        try:
            sequence += [int(i) for i in input().split()]
            if sequence[-1] == -999999:
                sequence.pop(-1)
                break
        except EOFError:
            break

    n = sequence.__len__()

    if n == 0:
        break

    positiveProduct = [0] * n
    negativeProduct = [0] * n

    positiveProduct[0] = max(positiveProduct[0], sequence[0])
    negativeProduct[0] = min(0, sequence[0])

    maxProduct = sequence[0]

    for length in range(1, n):
        positiveProduct[length] = max(0, sequence[length], positiveProduct[length-1]*sequence[length], negativeProduct[length-1] * sequence[length])
        negativeProduct[length] = min(0, sequence[length], positiveProduct[length-1]*sequence[length], negativeProduct[length-1] * sequence[length])
        maxProduct = max(positiveProduct[length], negativeProduct[length], maxProduct)

    print(maxProduct)
    
