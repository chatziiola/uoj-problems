# Seems like a regular case of comparison sort

cases = int (input())

while cases:

    try:
        wagons = int(input())
        wagonList = [int(i) for i in input().split()]
    except EOFError:
        break

    swaps = 0
    
    # Unfortunately my algorithm here is 0(n^2), but necessary due to comparison sort
    for wagonNumber in range(1,wagons+1):
        # Find the current position of wagon number. Since we go from 1 to wagons it is true that
        # it can not be before the final position 
        for position in range(wagonNumber-1, wagons):
            if wagonList[position] == wagonNumber:
                while position != wagonNumber-1:
                    tmp = wagonList[position]
                    wagonList[position] = wagonList[position -1]
                    wagonList[position -1] = tmp
                    position -= 1
                    swaps +=1
                break

    print(f"Optimal train swapping takes {swaps} swaps.")
    cases -= 1
