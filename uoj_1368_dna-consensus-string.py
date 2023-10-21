cases = int(input())

while cases:
    # m: number of sequences
    # n: length of sequences
    m,n = [int(i) for i in input().split()]

    # Store the sequences
    sequences = []
    for i in range(m):
        sequences.append(input())

    consensusString = []
    consensusError = 0

    # The algorithm I'm thinking of (maybe too simplistic), is O(mxn)
    # For every character
    for index in range(n):
        # Create a map for all possible characters: ACTG
        characterMap = {"A":0, "C": 0, "G":0, "T":0}
        for seq in range(m):
            characterMap[sequences[seq][index]] += 1
            #increase the corresponding map

        # find the character with the gratest number of iterations, if
        # there are two of them, alphabetically (thus, use the map in
        # alphabetic order)
        consensusLetter = "A"
        error = 0
        for letter in ["T","C","G"]:
            if characterMap[letter] > characterMap[consensusLetter]:
                error += characterMap[consensusLetter]
                consensusLetter = letter
            elif characterMap[letter]:
                error += characterMap[letter]
        consensusString.append(consensusLetter)
        consensusError += error 

    print("".join((consensusString)))
    print(consensusError)

    cases -= 1
