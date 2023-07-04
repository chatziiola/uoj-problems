# Radar installation
from math import sqrt

case = 1
while True:
    allIslandsCanBeCovered = True
    islands = []
    try:
        n, d = [int(i) for i in input().split()]
        if not n and not d:
            break
        for i in range(n):
            islands.append([int(u) for u in input().split()])
            # If the radar can not cover an island, even if placed at the closest point of land (x,0)
            if islands[i][1] > d:
                allIslandsCanBeCovered = False
        input()
    except EOFError:
        break

    # If all islands can be covered by a radar
    if allIslandsCanBeCovered:
        islands.sort()
        radars = 1

        minRadarX = [0] * n
        maxRadarX = [0] * n

        for island in range(n):
            # We have already checked that  d > y
            tmp = sqrt(d**2 - islands[island][1]**2) # d^2 - y^2

            # Now to be covered by a radar, the radar can at most be placed at minRadarX or maxRadarX
            # Anything in between is valid
            maxRadarX[island] = islands[island][0] + tmp
            minRadarX[island] = islands[island][0] - tmp

            if island == 0:
                radar = maxRadarX[island]

            # Since the island array is sorted, this is the only check we need to make
            # radar < Bmin
            if radar < minRadarX[island]:
                radar = maxRadarX[island]
                radars += 1
            else:
                # Bmin <  radar <= B < Bmax
                if islands[island][0] < radar:
                    radar = min(maxRadarX[island], radar)
                # otherwise the existing radar best covers the set of islands as they are.
    else:
        radars = -1

    
    print(f"Case {case}: {radars}")
                        
    # print(f"\n\n\n")
    case += 1
