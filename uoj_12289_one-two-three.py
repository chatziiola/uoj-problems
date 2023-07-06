# seems tedious, and i don't think a particularly efficient algorithm exists

cases = int(input())

while True:
    try:
        s = input()
    except EOFError:
        break
    if len(s) == 5:
        print(3)
    else:
        # Checking for one:
        one = 0
        if s[0] == "o":
            one += 1
        if s[1] == "n":
            one += 1
        if s[2] == "e":
            one += 1
        if one >= 2:
            print(1)
        else:
            print(2)
