# BFS
# UOJ 459
from queue import deque

cases = int(input())

input() # Blank Line

for case in range(1, cases+1):

    try:
        lastNode = input()
    except EOFError:
        break

    # Create adjacency list dynamically
    myGraph = {chr(i): [] for i in range(ord('A'), ord(lastNode) + 1)}
    traversed = set()

    while True:
        try:
            line = input()
            if line.__len__() == 0:  # That would mean empty line
                break
            myGraph[line[0]].append(line[1])
            myGraph[line[1]].append(line[0])
        except EOFError:
            break

    unconnectedGraphs = 0

    for node in myGraph:
        if node in traversed:
            continue
        unconnectedGraphs += 1

        Q = deque(node)
        while Q:
            tempnode = Q.popleft()
            traversed.add(tempnode)
            for neighbor in myGraph[tempnode]:
                if neighbor not in traversed:
                    traversed.add(neighbor)
                    Q.append(neighbor)

    # Print empty line
    if case > 1:
        print()

    print(unconnectedGraphs)
