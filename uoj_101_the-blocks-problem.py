numberOfBlocks = int(input())

currLocation = [int(i) for i in range(numberOfBlocks)]
blocks = [list([i]) for i in range(numberOfBlocks)]

## Validated
# Does not work properly, when l is the top element
def clearOnTopOf(l):
    '''Delete all elements on top of l moving them to their default position. Does not delete l'''
    # Find the location of value
    valueIndex = 0
    for i in range(len(blocks[currLocation[l]])):
        if blocks[currLocation[l]][i] == l:
            valueIndex = i
            break
    tmpArr = blocks[currLocation[l]][valueIndex+1:]
    blocks[currLocation[l]] = blocks[currLocation[l]][:valueIndex+1]

    for i in range(len(tmpArr)):
        currLocation[tmpArr[i]] = tmpArr[i]
        blocks[tmpArr[i]] = [tmpArr[i]]

def pile(a,b):
    '''Move stack on top of A to the stack where B is'''
    valueIndex = 0
    for i in range(len(blocks[currLocation[a]])):
        if blocks[currLocation[a]][i] == a:
            valueIndex = i
            break
    tmpArr = blocks[currLocation[a]][valueIndex:]
    blocks[currLocation[a]] = blocks[currLocation[a]][:valueIndex]
    for i in tmpArr:
        blocks[currLocation[b]].append(i)
        currLocation[i] = currLocation[b]

def move(a,b):
    '''Move only a on top of B's location(may clear elements)'''
    clearOnTopOf(a)
    # Delete a
    blocks[currLocation[a]] = blocks[currLocation[a]][0:-1]
    currLocation[a] = currLocation[b]
    blocks[currLocation[b]].append(a)
    blocks[a] = []
    # else:
        # Move a on top of the stack in which b exists, anything on top of a goes to initial position


while True:
    try:
        command, a, arg, b = input().split()
    except ValueError:
        break # This also catches quit I hope

    a = int(a)
    b = int(b)

    # Check for illegal commands
    # print(f"{a} {command},{arg} {b}")
    if a == b or currLocation[a] == currLocation[b]:
        # print("\tIllegal Move")
        continue;

    if arg == "onto":
        clearOnTopOf(b)

    if command == "move":
        move(a,b)
    else:
        pile(a,b)
    # print(blocks)

for index in range(numberOfBlocks):
    print(f"{index}:",end="")
    for element in blocks[index]:
        print(f" {element}",end="")
    print()

