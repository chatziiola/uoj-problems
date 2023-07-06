# Maximum Subsequence
from bisect import bisect


while True:
    try:
        s, t = input().split()
    except EOFError:
        break

    dictionary = {chr(char): list([]) for char in range(ord('a'), ord('z')+1)}
    dictionary.update({chr(char): list([]) for char in range(ord('A'), ord('Z')+1)})
    
    # O(n)
    for index in range(len(t)):
        dictionary[t[index]].append(index)

    lastIndex = 0
    possibol = True
    # O(nlgn)
    for character in s:
        pos = bisect(dictionary[character], lastIndex)
        if pos == len(dictionary[character]):
            possibol = False
            break
        else:
            lastIndex = dictionary[character][pos]

    if possibol :
        print("Yes")
    else:
        print("No")
