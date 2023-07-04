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

# The algorithm:
# For every number:
# the maximum subsequence up until (including) that number can only be:
# the maximum subsequence of the last number that's lowest than number + the number
# and the length will be +1

# This algorithm runs in O(n^2). Can it be improved?
# Ideas:
## array lastindexof[no], last occurence of no in input
## - max subseq of that ...
## - also in O(n^2), but more pruning.

# Instead of storing multiple arrays
subseqLength = [1] * n
previousIndex = [-1] * n


maxLenIndex = 0
currMaxLength = 0

# This algorithm runs in an obvious O(n^2):
# - I could prune it, and I can think of a /clever/ solution with pruning, but I'm not sure as to whether that would be helpful
for index in range(n):
    # print(f"Checking: ({index})")
    for l in range(index):
        # print(f"\t @({index}) with {l}:")
        if inputseq[l] < inputseq[index] and \
           subseqLength[l] >= subseqLength[previousIndex[index]]:
            # print(f"\t\t @({inputseq[index]}) greater than {inputseq[l]}:")
            subseqLength[index] = subseqLength[l] + 1
            previousIndex[index] = l
            if subseqLength[index] >= currMaxLength:
                maxLenIndex = index
                currMaxLength = subseqLength[index]
    

# print(f"Input:\t\t{inputseq}\nSubseqLength:\t\t{subseqLength}\nPrevious Index\t\t{previousIndex}")
print(currMaxLength)

print("-")

def myprint(index):
    if index == -1: return
    else:
        myprint(previousIndex[index])
        print(inputseq[index])
    

myprint(maxLenIndex)
