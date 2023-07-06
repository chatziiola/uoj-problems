# I'm thinking of creating an array of stacks:
# - n-1 spaces:
#   - if stack[n] is not empty


### Step by step on the input
 #| A | B | Step     | 0 | 1         | 2 | 3 | 4 |       5 |     6 | 7 | 8 | 9 |
 #|---+---+----------+---+-----------+---+---+---+---------+-------+---+---+---|
 #|   |   |          | 0 | 1         | 2 | 3 | 4 |       5 |     6 | 7 | 8 | 9 |
 #| 9 | 1 | MoveOnto | 0 | 1,9       | 2 | 3 | 4 |       5 |     6 | 7 | 8 |   |
 #| 8 | 1 | MoveOver | 0 | 1,9,8     | 2 | 3 | 4 |       5 |     6 | 7 |   |   |
 #| 7 | 1 | MoveOver | 0 | 1,9,8,7   | 2 | 3 | 4 |       5 |     6 |   |   |   |
 #| 6 | 1 | MoveOver | 0 | 1,9,8,7,6 | 2 | 3 | 4 |       5 |       |   |   |   |
 #| 8 | 6 | pileOver | 0 | 1,9       | 2 | 3 | 4 |       5 | 8,7,6 |   |   |   |
 #| 8 | 5 | pileOver | 0 | 1,9       | 2 | 3 | 4 | 5,8,7,6 |       |   |   |   |
 #| 2 | 1 | moveOver | 0 | 1,9,2     |   | 3 | 4 | 5,8,7,6 |       |   |   |   |
 #| 4 | 9 | moveOver | 0 | 1,9,2,4   |   | 3 |   | 5,8,7,6 |       |   |   |   |

# The above shows me that there is something peculiar:
## Need to maintain location of all elements
## why does pile 8 over 6 simply move to the blank 6 instead of going 6,7,8?

numberOfBlocks = int(input())

currLocation = [int(i) for i in range(numberOfBlocks)]
blockPositions = [list([]) * numberOfBlocks]

def move(a,b,arg):
    '''Move only a'''
    if arg == "onto":
        # Move a on top of b, while returning anything on a,b to their initial positions
        print("move onto")
    else:
        # Move a on top of the stack in which b exists, anything on top of a goes to initial position
        print("move over")


def pile(a,b,arg):
    '''Move the stack on top of a'''
    if arg == "onto":
        # Move the stack of a on top of b, while returning anything on b to their initial positions
        print("pile onto")
    else:
        # Move the stack of a on top of the stack of b
        print("pile over")



while True:
    try:
        command, a, arg, b = input().split()
    except ValueError:
        break # This also catches quit I hope

    if command == "move":
        move(a,b,arg)
    else:
        pile(a,b,arg)

