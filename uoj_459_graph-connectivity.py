import queue


class Graph:
    '''Just a graph class'''
    def __init__(self, endid):
        self.endnode = endid
        self.nodes = [Node(letter) for letter in range(ord('A'), endid+1)]

    def idToCell(self, id):
        return id - 65

    def indexNode(self, id):
        self.nodes[self.idToCell(id)].indexed()

    def addVertex(self, start, end):
        self.nodes[self.idToCell(start)].addNeighbor(self.idToCell(end))

    def getTopNode(self):
        return self.nodes.pop()

    def getNodeWithID(self, id):
        return self.nodes[self.idToCell(id)]

    def notEmpty(self):
        return self.nodes.__len__() > 0

class Node:
    '''Just a node class'''
    def __init__(self, id):
        self.id = id
        self.adjacencyList = []
        self.indexed = False

    def getIndexedStatus(self):
        '''Return whether this node has been toindex'''
        return self.indexed

    def indexed(self):
        '''Set toindex to True'''
        self.indexed = True

    def getid(self):
        '''Get letter associated with node, but in ASCII code'''
        return self.id

    def addNeighbor(self, neighborsid):
        '''Add neighbor'''
        self.adjacencyList += [neighborsid]

    def getNeighbors(self):
        '''Get neighbor'''
        return self.adjacencyList


cases = int(input())
input()  # Blank Line
 
for case in range(1,cases+1):
    # Set graph with max node 
    myGraph = Graph(ord(input()))

    # Handle input
    while True:
        line = input()
        if line.__len__() == 0:
            break
        myGraph.addVertex(ord(line[0]),ord(line[1]))
    
    # Traverse, calculate answer
    answer = 0
    Q = queue.Queue()

    while myGraph.notEmpty():
        answer += 1
        Q.put(myGraph.getTopNode())
        while not Q.empty():
            currentNode = Q.get()
            for i in currentNode.getNeighbors():
                # Πάλι δεν βγαίνει - μάλλον το έκανα υπερβολικά σύνθετο. Όταν γυρ΄σω απλά
                
                Q.put(myGraph.getNodeWithID(i))

    # Empty line in output
    if case > 1:
        print()

    print(answer)
