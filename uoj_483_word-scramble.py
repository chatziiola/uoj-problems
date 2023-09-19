# Seems rather tedious
import re

while True:
    try:
        message = input()
    except EOFError:
        break


    words = re.split(r'(\s+)', message)

    # print(words)
    for word in words:
        for index in range(-1,-len(word)-1,-1):
            print(word[index],end="")
        # if word != words[-1]:
        #     print(" ", end="")

    # print(message) # WTF

    print()
