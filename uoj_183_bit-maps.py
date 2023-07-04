import re
import textwrap
import queue
from math import ceil,floor

ones_pattern = re.compile("^1+$")
zeroes_pattern = re.compile("^0+$")

inputInd = 0
inputMap = ""
outpmap = []
inqueue = []

def printMatrix(matrix):
    for row in matrix:
        print(row)  # Print a new line after each row

def bToD(bitmap,rows,columns):
    if len(bitmap) == 0:
        return ""
    if ones_pattern.match(bitmap):
        return "1"
    elif zeroes_pattern.match(bitmap):
        return "0"
    else:
        upperRows = ceil(rows/2)
        upperColumns = ceil(columns/2)

        # Upper Left
        bm = ""
        for line in range(upperRows):
            startingPoint = columns*line
            bm += bitmap[startingPoint: startingPoint+upperColumns]

        answ1 = bToD(bm, upperRows, upperColumns)

        # Upper Right
        bm = ""
        for line in range(upperRows):
            startingPoint = columns*line
            bm += bitmap[startingPoint+upperColumns: startingPoint+columns]

        answ2 = bToD(bm, upperRows, columns-upperColumns)

        # Bottom Left
        bm = ""
        for line in range(upperRows, rows):
            startingPoint =  columns*line
            bm += bitmap[startingPoint: startingPoint+upperColumns]

        answ3 = bToD(bm, rows-upperRows, upperColumns)

        # Bottom Right
        bm = ""
        for line in range(upperRows, rows):
            startingPoint =  columns*line
            bm += bitmap[startingPoint+upperColumns: startingPoint+columns]

        answ4 = bToD(bm, rows-upperRows, columns-upperColumns)

        return "D"+answ1+answ2+answ3+answ4


# Now this is problematic
def dToB(rowsS, rowsE, colsS, colsE):
    '''Transforms the input d-string, located in inputmap, into its bstring alternative.
    This recursive function utilizes:
    - ***S: start
    - ***E: end
    - ***H: half'''

    global inqueue, inputMap, outpmap

    if rowsS == rowsE or colsS == colsE:
        return

    command = inqueue.popleft()

    # print(f"Command: {command}")
    # print(f"\tWorking on ({rowsS}-{rowsE},{colsS}-{colsE})")

    if command == '1':
        for line in range(rowsS,rowsE):
            for col in range(colsS,colsE):
                outpmap[line][col] = 1

    elif command == '0':
        for line in range(rowsS,rowsE):
            for col in range(colsS,colsE):
                outpmap[line][col] = 0
    elif command == 'D':
        rowsH = ceil((rowsS+rowsE)/2)
        colsH = ceil((colsS+colsE)/2)
        # print(f"\tSubdividing:\t({rowsS}-{rowsH},{colsS}-{colsH})\t({rowsS}-{rowsH}, {colsH}-{colsE})")
        # print(f"\t\t\t({rowsH}-{rowsE}, {colsS}-{colsH})\t({rowsH}-{rowsE}, {colsH}-{colsE})")

        dToB(rowsS, rowsH, colsS, colsH)
        dToB(rowsS, rowsH, colsH, colsE)
        dToB(rowsH, rowsE, colsS, colsH)
        dToB(rowsH, rowsE, colsH, colsE)
    # print(f"\tEnding: ")
    # printMatrix(outpmap)


while True:
    try:
        line = input()
        if line[0] == '#':
            break
        format = line[0]
        rows, columns = [int(i) for i in line[1:].split()]
        inputMap = ''
        if format == 'B':
            while len(inputMap) < rows*columns:
                inputMap += input()
        else:
            inputMap = input()
                
    except EOFError:
        break

    if format == 'B':
        print(f"D{rows:4d}{columns:4d}")
        print(textwrap.fill(bToD(inputMap, rows, columns), width=50))
    else:
        print(f"B{rows:4d}{columns:4d}")
        inqueue = queue.deque(inputMap)
        # print(inputMap)
        outpmap = [list(["joke"]*columns) for i in range(rows)]
        dToB(0,rows,0,columns)

        answer = ''
        for line in range(rows):
            answer += ''.join(map(str, outpmap[line]))

        print(textwrap.fill(answer, width=50))
