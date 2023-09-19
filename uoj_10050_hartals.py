# Also tedious:
cases = 1+int(input())
# print(f"Cases: {cases}")

for cs in range(1,cases):
    # If number of days is 15, and we start from 0, we have to reduce
    # by -1. That is not necessary. We can simply increment n by one,
    # since the beginning line is always 0
    print(f"Case: {cs}")
    n = int(input())
    p = int(input())
    print(f"Number of days: {n}")
    print(f"Number of parties: {p}")

    bitmap = [False]*(n+1)
    lostDays = 0;

    # We do not count sundays as lost days
    for week in range(n//7):
        bitmap[week*7+1] = True
    if (n > (n//7)*7):
        bitmap[7*(n//7)+1] = True
        

    # In fact this should be much simpler.
    for party in range(p):
        partyHartal = int(input())
        print(f"Hartal is {partyHartal}")
        for coef in range(1,(n-1)//partyHartal+1):
            # print(f"{coef*partyHartal}", end=",")
            if bitmap[coef*partyHartal]:
                continue
            bitmap[coef*partyHartal] = True
            lostDays +=1
        # print()

    for week in range(n//7):
        for day in range(1,8):
            print(f"\t{day+week*7}: {bitmap[week*7+day]}",end="")
        print()
    for day in range(7*(n//7)+1, n+1):
        print(f"\t{day}:{bitmap[day]}", end="")
    print()
    

    print(lostDays)

    cases -= 1
