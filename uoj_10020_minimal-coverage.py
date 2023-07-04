# We want to cover [0,M], using segments from [L_i,R_i]
# Separated by blank line
from queue import deque

class Node:
    def __init__(self):
        self.visited = False
        self.parent = 0
        self.distance = 0

cases = int(input())

for case in range(cases):
    adjacencyList = {i:[] for i in range(100000)}
    nodes = [Node() for i in range(100000)]

    # Handle Input
    # I change it to /base/ 50000 to deal with negative numbers
    try:
        input()  # Blank line
        M = int(input()) + 50000
        while True:
            L,R = [ int(i) for i in input().split() ]
            if L == 0 and R == 0:
                break
            adjacencyList[R+50000].append(L+50000)
    except EOFError:
        break

    if case > 0:
        print()

    for i in range(100000):
        if adjacencyList[i]:
            print(f"Paths to {i}: {adjacencyList[i]}")

    Q = deque([M])
    nodes[M].visited = True
    nodes[M].distance = 0

    startingNode = 50000

    while Q:
        currentNode = Q.popleft()
        print(f"curr node: {currentNode}")
        if currentNode < 50001:
            startingNode = currentNode
            break
        for neighbor in adjacencyList[currentNode]:
            print(f"\tNeighbor node: {neighbor}")
            print(f"\t{nodes[neighbor].visited} {nodes[neighbor].distance} {nodes[neighbor].parent}")
            if not nodes[neighbor].visited:
                Q.append(neighbor)
                nodes[neighbor].parent = currentNode
                nodes[neighbor].distance = nodes[currentNode].distance + 1
                nodes[neighbor].visited = True
    # OUTPUT
    print(nodes[startingNode].distance)
    if nodes[startingNode].distance > 0:
        currentNode = startingNode
        while True:
            if currentNode == nodes[currentNode].parent:
                # print("MALAKIA")
                break
            print(f"{currentNode-50000} {nodes[currentNode].parent-50000}")
            currentNode = nodes[currentNode].parent
            if currentNode == M:
                break
