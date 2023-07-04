# Right, after reading the problem:
# We want to create a graph:
# - Directed: if domino falls, graph[dominos] fall as well (and their /subdominoes/ too)
from queue import deque

cases = int(input())

for case in range(cases):
    # Get input
    try:
        n, m, l = [int(i) for i in input().split()]

        graph = {i: [] for i in range(1, n+1)}
        drops = []

        # Links
        for i in range(m):
            line = [int(i) for i in input().split()]
            graph[line[0]].append(line[1])

        # Drops
        for i in range(l):
            drops.append(int(input()))

    except EOFError:
        break

    fallenDominoes = 0

    visited = set()

    while drops:
        q = deque([drops.pop()])

        while q:
            node = q.popleft()
            if node in visited:
                continue
            fallenDominoes += 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)
            visited.add(node)

    print(fallenDominoes)
