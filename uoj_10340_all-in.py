# Maximum Subsequence

while True:
    try:
        s, t = input().split()
    except EOFError:
        break

    i = 0
    for char in t:
        if char == s[i]:
            i += 1
            if len(s) == i:
                break

    if  i == len(s):
        print("Yes")
    else:
        print("No")
