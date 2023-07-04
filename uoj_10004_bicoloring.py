from queue import deque
# This is an interesting graph problem (easy enough )


# I will store my graph in an adjacency list.

# Idea: a graph is NOTBICOLORABLE, if there exists a path from any
# given node, to another, with an odd path cost.

while True:
    try:
        # number of nodes
        n = int(input())
        if n == 0:
            break

        # number of edges
        l = int(input())

        adjacencyList = [set([]) for i in range(n)]  

        for i in range(l):
            a,b = [int(z) for z in input().split()]
            # Nondirected graph
            adjacencyList[a].add(b)
            adjacencyList[b].add(a)

    except EOFError:
        break

    colors = [0] * n
    colors[0] = 1
    bicolorable = True

    Q = deque([0])
    
    while len(Q)>0 and bicolorable:
        node = Q.popleft()
        for neighbor in adjacencyList[node]:
            if colors[neighbor] == colors[node]:
                bicolorable = False
                break
            elif colors[neighbor] == 0:
                colors[neighbor] = (-1)*colors[node]
                Q.append(neighbor)
            
        if not bicolorable:
            break

    if bicolorable:
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")
