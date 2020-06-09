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

    if currID == 26:
        for i in range(26):
            ids[i] = ids[i][0] + str(int(ids[i][1:]) + 1)
        currID = 1
        return ids[0]
    else:
        currID += 1
        return ids[currID]

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

        print("Graph %s Out:" % (q + 1))
        for i in range(N):
            print('\t' + "Node " + str(i) + ":")
            for j in range(len(adjOut[i])):
                print('\t\t' + "Edge %s: " % (adjOut[i][j].id) + "Destination: %s " % (adjOut[i][j].child) + "Start Time: %s " % (adjOut[i][j].startTime) + "End Time: %s " % (adjOut[i][j].endTime) + "Weight: %s " % (adjOut[i][j].weight))
            print()
        print("Graph %s In:" % (q + 1))
        for i in range(N):
            print('\t' + "Node " + str(i) + ":")
            for j in range(len(adjIn[i])):
                print('\t\t' + "Edge %s: " % (adjIn[i][j].id) + "Destination: %s " % (adjIn[i][j].child) + "Start Time: %s " % (adjIn[i][j].startTime) + "End Time: %s " % (adjIn[i][j].endTime) + "Weight: %s " % (adjIn[i][j].weight))
        print()
        print()
        print()

generateGraph(6,1.5,(0,8),1)