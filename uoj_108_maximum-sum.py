# Now this one seems tricky: find the maximum subrectangle of a given
# matrix.If NxN are the dimensions of the matrix, I think it is
# reasonable to assume a lowerbound of omega(n^2)

# I thought of following a divide and conquer (greedy) methodology:
# It obviously does not work, but I was wondering if there is something to build on:
# - find max in every half
#   - if both positive:
#     - if they can be combined
#       combine
#   - else:
#     - max = max(each half)


# O(n).Kadane's Algorithm for max sum in 2d: easily understood: iterate
# through the array, while keeping a "maxsumtillhere", and a
# "totalmaxsum": if maxsumtillhere<0, set it to zero, otherwise move
# to next.

# How can this be implemented for a 2-d matrix?
## First of all: Kadane will need to be modified to work within limits and to return limits:
### given (start,end,array)
### get(start,end, max)
## where, since we are in 2 dimensional array: start = (sR,sC,) end = (eR,eC)
## So finally given(sR,sC,eR,eC,array), get(sR,sC,eR,eC,array)

## And how will the data be compared?

## Kadane on each row and then comparing is not good enough: But
## Kadane can be implemented in each of the O(n^2) combinations of
## columns
def kadane_2d(matrix):
    n = len(matrix)
    maxSum = float('-inf')
    left = right = top = bottom = 0

    # Iterate the matrix for every column starting on the left
    for leftCol in range(n):
        # Used to hold the sum of all elements from leftcol to rightcol in each row
        tempRowSum = [0] * n

        # for every column combination (start @leftcol - stop @rightcol)
        for rightCol in range(leftCol, n):

            # tempRow, essentially is the sum of all `
            for row in range(n):
                tempRowSum[row] += matrix[row][rightCol]

            # Essentially KADANE
            tempSum = 0
            currTop = 0
            for currBottom in range(n):
                tempSum += tempRowSum[currBottom]
                if tempSum > maxSum:
                    maxSum = tempSum
                    left = leftCol
                    right = rightCol
                    top = currTop
                    bottom = currBottom
                if tempSum < 0:
                    tempSum = 0
                    currTop = currBottom + 1

    return maxSum #, (left, top), (right, bottom)

# Not one case
while True:
    try:
        n = int(input())
    except EOFError:
        break

    tempArray = []
    myArray = []

    # read Input
    while len(tempArray) < n**2:
        try:
            tempArray += [int(i) for i in input().split()]
        except EOFError:
            break

    # Fix input in matrix
    for i in range(n):
        myArray.append(tempArray[i*n:(i+1)*n])


    print(kadane_2d(myArray))
