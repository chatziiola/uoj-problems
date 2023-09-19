# 230905/230906
from queue import deque

### Since we want the maximum number of directly connected cities that
### have the maximum average PPA and that is given (as the maximum PPA
### found in any route) in input, all we have to do is search (DFS,
### BFS) through all the nodes, and see if a road with a maximum PPA
### value exists. If yes, follow the path, otherwise, the path ends
### there

### The reason why that algorithm works is the phrase *maximum
### possible PPA* in the definition of the problem. If we fall below
### that, there is no way for us to go back at it (otherwise it would
### not be the maximum possible PPA in the first place).

# (It turns out that this was a good logical, yet slightly hasty
# solution. I should have tried to express it in terms of computer
# science: Being a graph like that, I could have gone either for BFS
# or DFS, since I'm only looking for a path:
## My solution essentially is DFS, with a *very important* path
## elimination constraint: PPA value)


class City:
    # Adjacency list holds pairs in the form of
    # [destination, cost]
    adjacency_list = []
    visited = False

    def __init__(self):
        self.adjacency_list = list()
        self.visited = False


while True:
    # N: Cities
    # M: Roads
    try:
        n,m = [int(i) for i in input().split()]
    except EOFError:
        break

    if n == 0 and m == 0:
        break

    citiesArray = [City() for i in range(n+1)]

    myPPA = - float('inf')
    myCities = 2

    for i in range(m):
        start, end, PPA = [int(l) for l in input().split()]
        myPPA = max(myPPA, PPA)
        citiesArray[start].adjacency_list.append([end, PPA])
        citiesArray[end].adjacency_list.append([start, PPA])

    for anycity in range(1, n+1):
        if citiesArray[anycity].visited:
            continue
        myQ = deque([anycity])

        # Θέλω μέχρι να πάω σε άλλο δίκτυο anycity να έχω το ίδιο counter
        currentProvinceSize = 0

        # DFS algorithm
        while len(myQ) > 0:
            city = myQ.pop()
            # That solves it
            if citiesArray[city].visited:
                continue
            currentProvinceSize += 1

            for neighboringCity in citiesArray[city].adjacency_list:
                # neighboringCity[0] = actual neighboringCity
                # neighboringCity[1] = PPA cost
                if neighboringCity[1] == myPPA and\
                   not citiesArray[neighboringCity[0]].visited:
                    myQ.append(neighboringCity[0])
                
            citiesArray[city].visited = True
            myCities = max(myCities, currentProvinceSize)

    print(myCities)
