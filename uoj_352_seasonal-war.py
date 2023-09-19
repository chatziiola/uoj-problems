# Simply need to check for adjacency between the matrix elements
# (I can't see how this is a graph)



# Algorithm: First things first: Storing the image Create a bool
# matrix of the same dim, defaults to false If a neigbor exists, set
# that value to true, and if no neighbors with True already as their
# value, increase the eagle count

case = 1

while True:
    try:
        lines = int(input())
    except EOFError:
        break

    eagles = 0
    image = []
    for i in range(lines):
        image.append(input())
    
    # Create the bool 
    for line in range(lines):
        for character in range(lines):
            if image[line][character] == '1':
                eagles += 1
                image[line][character] = '2'
            elif (image[max(0,line-1)][character] == '2'or \
                  image[min(lines-1, line+1)][character]== '2' or \
                  image[line][max(0,character-1)]== '2' or \
                  image[line][min(lines-1,character+1)] == '2'):
                    if image[line][character] = '0':
                        image[line][character] = '3'
                    if image[line][character] = '0':
                        image[line][character] = '3'
            elif image[line][character] == '1':
                eagles +=1

    # Print Image
    print("image")
    for line in range(lines):
        print(image[line])
    # Print Matrix
    print("matrix")
    for line in range(lines):
        print(boolMatrix[line])
        
    print(f"Image number {case} contains {eagles} war eagles.")
    case += 1
