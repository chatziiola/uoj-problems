# longest strictly increasing subseq
from bisect import bisect_left

inputseq = []

# Input
while True:
    try:
        inputseq.append(int(input()))
    except EOFError:
        break

n = len(inputseq)

# Fixing the algorithm up to work in nlogn (took inspiration from online)

mylist = [inputseq[0]]
posInOutput = [0]
outputLength = 0

for index in range(1,n):
    if mylist[-1] < inputseq[index]:
        mylist.append(inputseq[index])
        posInOutput.append(len(mylist)-1) 
        outputLength += 1
    else:
        tmp = bisect_left(mylist, inputseq[index])
        mylist[tmp] = inputseq[index]
        posInOutput.append(tmp)

# Now I plan to use mylist as my output array
mylist.clear()
for index in range(n-1,-1,-1):
    if posInOutput[index] == outputLength:
        mylist.insert(0, inputseq[index])
        # print(f"Sorting outp:\t {mylist}")
        outputLength -= 1
        if outputLength == -1:
            break

print(len(mylist))
print("-")
for l in mylist:
    print(l)
