# This seems rather tedious

# Taken from the definition
mirrored_dict = {'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '8': '8'}

while True:
    try:
        s = input()
    except EOFError:
        break

    palindrome = True
    mirrored = True

    # This works quite, well, but the problem is that it does not
    # properly check for the mirrored property: in the case of odd
    # length strings, the middle character is effectively unchecked.
    for index in range(len(s)//2 + 1):
        if s[index] != s[-1-index]:
            palindrome = False
        if s[index] not in mirrored_dict or \
           (s[index] in mirrored_dict and mirrored_dict[s[index]] != s[-1-index]):
            mirrored = False
        if not mirrored and not palindrome:
            break

    if palindrome and mirrored:
        print(f"{s} -- is a mirrored palindrome.")
    elif palindrome:
        print(f"{s} -- is a regular palindrome.")
    elif mirrored:
        print(f"{s} -- is a mirrored string.")
    else:
        print(f"{s} -- is not a palindrome.")
    print()
