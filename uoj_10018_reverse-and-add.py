
cases = int(input())

while cases:
    try:
        n = int(input())
    except EOFError:
        break

    additions = 0
    palindrome = False
    tmp = n

    digitArray = []
    # This now works:
    # Analysis:
    #### Outer loop runs (less than a thousand times, according to the definition)
    #### First inner loop: less than 5 repetitions (definition)
    #### Second inner loop: less than 10 repetitions (definition)

    # Not perfect, but given the nature of the problem, I do not think
    # there is a reason to try and figure a better solution

    # till palindrome
    while not palindrome:
        digitArray.clear()
        # till n == 0:
        tmp = n
        while n > 0:
            # populate: digit_array
            digitArray.append(n%10)
            n = n // 10
        rank = len(digitArray)
        # check if n is a palindrome
        if additions: palindrome = True
        for i in range(rank//2):
            if digitArray[rank-1-i] != digitArray[i]:
                palindrome = False
                break
        # perform addition
        for i in range(rank):
            n += (digitArray[rank-1-i] + digitArray[i]) * 10**i
        # increase counter
        additions += 1


    print(f"{additions-1} {tmp}")

    #  if true continue



    # cases -= 1
