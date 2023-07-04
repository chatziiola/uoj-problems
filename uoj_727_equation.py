from queue import deque

cases = int(input())
a = False

input() # Empty line between cases and input

# O(n)
while cases:

    inputExpression = ""
    try:
        line = input()
        # If line is not empty
        while line:
            inputExpression += line
            line = input()
    except EOFError:
        a = True

    answer = ""

    stack = deque()

    # O(m), m <= 50
    for inputChar in inputExpression:
        # If our current character is an operator
        if inputChar == "+" or \
           inputChar == "-" or \
           inputChar == "*" or \
           inputChar == "(" or \
           inputChar == "/":

            # If addition, and there exists another operator in the stack:
            # TODO why?
            if len(stack) > 0 and\
               (inputChar == "+" or  inputChar == "-") and\
               stack[-1] != "(":
                answer += stack.pop()
                while len(stack) and\
                       (stack[-1] == "+" or stack[-1] == "-"):
                    answer +=stack.pop()

            # If multiplication and another multiplication
            # TODO why?
            elif len(stack) > 0 and\
                 (inputChar == "*" or  inputChar == "/") and\
                 (stack[-1] == "*" or stack[-1] == "/"):
                # Is this right?
                answer +=stack.pop()
            stack.append(inputChar)
        # Deal with the previous input, till ( is satisfied
        elif inputChar == ")":
            while stack[-1] != "(":
                answer += stack.pop()
            # Sketchy, remove the "("
            stack.pop()
        # Current character is a number, print it
        else:
            answer += inputChar

    # Sketchy but in case we have left overs
    while len(stack):
        tmpchar = stack.pop()
        if tmpchar != "(":
            answer += tmpchar

    cases -= 1
    print(f"{answer}")

    # Blank Line between cases`
    if cases:
        print()
    if a:
        break
