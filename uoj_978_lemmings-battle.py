# By definition, we want a structure that maintains order (from highest to lowest), on every round.

from queue import PriorityQueue

n = int(input())

while n:
    b, sg, sb = [int(i) for i in input().split()]

    greenSoldiers = PriorityQueue()
    blueSoldiers = PriorityQueue()

    ## Reverse , to get descending
    for i in range(sg):
        greenSoldiers.put(- int(input()))

    for i in range(sb):
        blueSoldiers.put(- int(input()))
    
    while True:
        tmpblue = []
        tmpgreen = []
        for i in range(b):
            # Equivalent to blue - green, but reversed due to - inside of queue.
            if greenSoldiers.empty() or blueSoldiers.empty():
                break
            win =  greenSoldiers.get() - blueSoldiers.get()
            # if 0 both of them die
            if win > 0:
                tmpblue.append(-win)
            elif win < 0:
                tmpgreen.append(win)

        for i in tmpblue:
            blueSoldiers.put(i)
        for i in tmpgreen:
            greenSoldiers.put(i)

        if greenSoldiers.empty() or blueSoldiers.empty():
            break


    if greenSoldiers.empty() and blueSoldiers.empty():
        print("green and blue died")
    elif greenSoldiers.empty():
        print("blue wins")
        while not blueSoldiers.empty():
            print(- blueSoldiers.get())
    else:
        print("green wins")
        while not greenSoldiers.empty():
            print(- greenSoldiers.get())

    n -= 1
    if n:
        print()
