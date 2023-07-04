# obviously I will handle this with a stack approach.
# every character will be fed into the stack:
# if ( or [, plainly add to the stack
# if ) or ], pop from the stack, and compare pair
# - if pair valid, we don't have to do anything
# - else, set to false, move to next case


# Stack in python: deque
from queue import deque

cases = int(input())

while True:
    try:
        line = input()
    except EOFError:
        break


    correct = True
    mystack = deque([])

    # O(n)
    for char in line:
        if char == "(" or char == "[":
            mystack.append(char)
        else:
            if len(mystack) > 0:
                openPair = mystack.pop()
                if (openPair == "(" and char == "]") or openPair == "[" and char == ")":
                    correct = False
                    break
            else:
                    correct = False
                    break

    if len(mystack) > 0:
        correct = False
        
    if correct:
        print("Yes")
    else:
        print("No")

# I don't do so well in terms of time performance in the uoj, but, i
# think that it is more due to the nature of python than due to my
# analytical skills
