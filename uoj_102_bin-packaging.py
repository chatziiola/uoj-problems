import sys

class bottles:
    bins = []

    def __init__(self, a,b,c):
        self.bins = [a,b,c]

    def moveto(self,bin):
        return (sum(self.bins, (-1) * self.bins[bin]))

for line in sys.stdin:
    inputarray = []
    inputarray.extend(map(int,line.strip().split()))

    binarray = [bottles(inputarray[0], inputarray[3], inputarray[6]), #blue
                bottles(inputarray[1], inputarray[4], inputarray[7]), #green
                bottles(inputarray[2], inputarray[5], inputarray[8])] #clear

    cost = sum(inputarray)
    mycomb = 'BCG'

    for comb in ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']:
        tmpcost = 0
        for targbin in range(0,3):
            if comb[targbin] == 'B':
                tmpcost += binarray[0].moveto(targbin)
            elif comb[targbin] == 'G':
                tmpcost += binarray[1].moveto(targbin)
            elif comb[targbin] == 'C':
                tmpcost += binarray[2].moveto(targbin)
        if  tmpcost < cost:
            mycomb = comb
            cost = tmpcost
    print(f"{mycomb} {cost}")
