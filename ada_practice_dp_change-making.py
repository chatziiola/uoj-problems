# Problem: Given an unlimited supply of coins of denominations 
# x_1,x_2 ... x_n, we need to make change of a value of v using the
# minimum number of coins. 

# This problem is a classic application of DP:
# - We want to split the problem into smaller subproblems
# - and then build the total out of those smaller ones

v = 99
x = [1, 2, 5, 10, 20, 50]

coins = [0] * (v+1)

# Populate the coins array 
for i in range(1, v+1):
    # print(f"I is {i}")
    tmp = coins[i-x[0]]
    # print(f"Tmp is {tmp}")
    for coin in x:
        if i-coin < 0:
            break
        # print(f"Tmp is min({tmp},{coins[i-coin]}): {tmp}")
        tmp = min(tmp, coins[i-coin])
    coins[i] = 1 + tmp
    # print(f"Coins is {coins[i]}")

print(f"Minimum number of coins for {v} is: {coins[v]}")
