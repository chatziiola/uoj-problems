# longest strictly increasing subseq

inputseq = []

# Input
while True:
    try:
        inputseq.append(int(input()))
    except EOFError:
        break


# The algorithm:
# For every number:
# - if the previous number is smaller than that, longest subseq including that number is +1
# - else it is 1 (only includes itself)

n = len(inputseq)

maxsubeqs = [1]*n
finalmax = 0

for i in range(1, n):
    if inputseq[i] > inputseq[i-1]:
        maxsubeqs[i] = maxsubeqs[i-1] + 1
        if maxsubeqs[i] > maxsubeqs[finalmax]:
            finalmax = i

# Length
print(f"{maxsubeqs[finalmax]}")

# Presentation
print("-")

# Output
for i in inputseq[finalmax+1-maxsubeqs[finalmax]:finalmax+1]:
    print(i)


