from random import randint

ids = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'i1', 'j1', 'k1', 'l1', 'm1', 'n1', 'o1', 'p1', 'q1', 'r1', 's1', 't1', 'u1', 'v1', 'w1', 'x1', 'y1', 'z1']
idsCopy = ids
currID = -1

class Edge:
    def __init__(self,weight,startTime,endTime,parent,child,id):
        self.weight = weight
        self.startTime = startTime
        self.endTime = endTime
        self.parent = parent
        self.child = child
        self.id = id

def generateID():
    global ids
    global currID

    if currID > 25:
        for i in range(26):
            ids[i] = ids[i][0] + str(int(ids[i][1:]) + 1)
        currID = 1
        return ids[0]
    else:
        currID += 1
        return ids[currID - 1]

def resetIDs():
    global ids
    global idsCopy

    ids = idsCopy

def convertOutToIn(adj,n):
    newAdj = []
    for i in range(n):
        newAdj.append([])

    for i in range(n):
        for j in range(len(adj[i])):
            newAdj[adj[i][j].child].append(adj[i][j])

    return newAdj

def generateGraph(N, density, timeRange, count):
    for q in range(count):

        adjOut = []
        for i in range(N):
            adjOut.append([])

        for i in range(int(N * density)):
            weight = randint(0,25)
            startTime = randint(timeRange[0],timeRange[1] - 1)
            endTime = randint(startTime + 1, timeRange[1])
            parent = randint(0,N - 1)
            child = randint(0,N - 1)
            id = generateID()

            edge = Edge(weight, startTime, endTime, parent, child, id)
            adjOut[parent].append(edge)

        adjIn = convertOutToIn(adjOut, N)

        resetIDs()

        file = open("Graph%s.txt"  % (q),"w")

        file.write(str(N) + '\n')
        for i in range(len(adjOut)):
            for j in range(len(adjOut[i])):
                edge = adjOut[i][j]
                line = str(edge.id) + ',' + str(edge.weight) + ',' + str(edge.startTime) + ',' + str(edge.endTime) + ',' + str(edge.parent) + ',' + str(edge.child)
                file.write(line + '\n')

        file.close()

generateGraph(19700,2.23350254,(0,24),1)