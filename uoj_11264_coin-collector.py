# We want to maximize *different* types of coins while following the
# algorithm in withdrawal - find if an amount exists

cases = int(input())

while cases:
    try:
        n = int(input())
        c = [int(i) for i in input().split()]
    except EOFError:
        break

        
    # Maximum number of different coins you may collect if you collect
    # c[i] (included)
    maxNoOfSubcoins = [0]*n
    # Smallest sum to collect i and its maximum subcoins
    smallestSubcoinsSum = [c[n-1]]*n
    
    maxNoOfSubcoins[0] = 1
    smallestSubcoinsSum[0] = 1

    # DP/Greedy Solution
    # O(n^2) - Acceptable due to small n size but :/
    # print(f"{c}")
    for coin in range(1, n):
        nextCoinIndex = -1
        tmpMaxSubcoins = 0

        # print(f"Starting {coin}")
        for subcoin in range(0,coin):
            # If that subcoin /array/ may be used
            # and if that subcoin /array/ has more coins than the current one
            if smallestSubcoinsSum[subcoin] < c[coin] \
               and maxNoOfSubcoins[subcoin] > tmpMaxSubcoins:
                if coin < n-1 and smallestSubcoinsSum[subcoin] + c[coin] >= c[coin+1]:
                    continue
                tmpMaxSubcoins = maxNoOfSubcoins[subcoin]
                nextCoinIndex = subcoin

        if nextCoinIndex > -1:
            maxNoOfSubcoins[coin] = 1 + maxNoOfSubcoins[nextCoinIndex]
            smallestSubcoinsSum[coin] = c[coin] + smallestSubcoinsSum[nextCoinIndex]
        else:
            maxNoOfSubcoins[coin] = 1
            smallestSubcoinsSum[coin] = c[coin]
        # print(f"\t{coin}: {c[coin]}, has {nextCoinIndex} for previous:\n\tsum:{smallestSubcoinsSum[coin]}\n\t{maxNoOfSubcoins[coin]}")
            
    print(f"{max(maxNoOfSubcoins)}")
    # print(f"\n\n--------------------------------------------------")
    cases -= 1
