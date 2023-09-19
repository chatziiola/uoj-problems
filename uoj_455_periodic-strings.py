import string
# import map

cases = int(input())

for case in range(cases):
    input() # blank line
    myString = input()

    # I want to find an algorithm that works with indices. Can this be
    # thought of as a divide and conquer problem? Not really, but
    ## Suppose that we have a string such as "abvsasdfabvsasdf":
    ## - If I know that it is periodic, I only 

    # 1. Iterate through the string, storing the index of each
    # occurence of a number in an ordered set map

    # 2. For every character
    ## From the list of current periods, eliminate any that don't fit

    # 3. If period substrings are left, keep the smallest one. Else
    # period is the length of the starting string
    startingPoints = [0]

    for index in range(1,len(myString)):
        if myString[0] == myString[index]:
            startingPoints.append(index)

    periodFound = False
    for index in range(1,len(myString)):
        currentChar = myString[index]
        if periodFound:
            break
        for startingPoint in startingPoints:
            try:
                if myString[startingPoint+index] != currentChar:
                    startingPoints.remove(startingPoint)
            except Exception:
                # print(f"Error: {case+1}")
                # print(f"Error: Index{index}, Length: {len(startingPoints)}")
                # print(f"Error: Input length: {len(myString)}")
                if (index)*len(startingPoints) == len(myString):
                    # print(f"\tFound smallest period")
                    periodFound = True
                else:
                    startingPoints.remove(startingPoint)
        
    # At this point, all we need is the second starting point
    if case:
        print()
    if len(startingPoints) > 1:
        print(f"{startingPoints[1]}")
    else:
        print(f"{len(myString)}")
