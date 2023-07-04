def validityCheck(reports, currentmonth):
    '''Check for validity '''
    for i in range(0, currentmonth+1):
        tmpsum = sum(reports[i:i+5])
        if not tmpsum < 0:
            # print(f"tmpsum: {tmpsum}")
            return False
    return True
                   
while True:
    try:
        s, d = [int(i) for i in input().split()]
    except EOFError:
        break

    monthlyReport = [s] * 12

    for currentmonth in range(0,8):
        last = currentmonth + 4
        # print(f"Starting {currentmonth} : {monthlyReport}")
        while not validityCheck(monthlyReport, currentmonth):
            monthlyReport[last] = -d
            last -= 1
            # print(f"\t Change: {currentmonth} : {monthlyReport}")

    answer = sum(monthlyReport)

    if answer > 0:
        print(answer)
    else:
        print("Deficit")

