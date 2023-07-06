# Given heights of N walls left to right:
# Find the total number of high and low jumps

t = int(input())

for case in range(1,t+1):
    try:
        n = int(input())
        walls = [int(i) for i in input().split()]
    except EOFError:
        break

    highj = 0
    lowj = 0
    
    for wall in range(0,n-1):
        if walls[wall] < walls[wall+1]:
            highj += 1
        elif walls[wall] > walls[wall+1]:
            lowj += 1

    print(f"Case {case}: {highj} {lowj}")
