while True:
    try:
        line = input()
    except EOFError:
        break

    myDict = {}

    for char_code in range(ord('A'), ord('Z') + 1):
        myDict[chr(char_code)] = 0

    # Add lowercase characters (a-z) to the dictionary
    for char_code in range(ord('a'), ord('z') + 1):
        myDict[chr(char_code)] = 0

    for myChr in line:
        if myChr.isalpha():
            myDict[myChr] += 1

    max = 0
    output = []
    for key in myDict:
        if myDict[key] > max:
            max = myDict[key]
            output = [key]
        elif myDict[key] == max:
            output.append(key)

    # for key in myDict:
    #     print(f"\t {key}, {myDict[key]}")

    answer = "".join(output)
    print(f"{answer} {max}")
    
