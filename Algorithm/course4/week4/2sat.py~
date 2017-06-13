import sys

invFtimes = {}

def createEdgeList(filename):
    f = open(filename)
    edgeList = []
    f.readline()
    for line in f:
        edgeList.append((int(line.split()[0]), int(line.split()[1])))
    f.close()
    return edgeList


def createAdjDict(edgeList):
    adjDict = {}
    revAdjDict = {}
    vertexSet = set()
    for head, tail in edgeList:
        if head not in vertexSet:
            vertexSet.add(head)
        if tail not in vertexSet:
            vertexSet.add(tail)
        if head not in adjDict:
            adjDict[head] = [tail]
        else:
            adjDict[head].append(tail)
        if tail not in revAdjDict:
            revAdjDict[tail] = [head]
        else:
            revAdjDict[tail].append(head)
    return adjDict, revAdjDict, vertexSet


def DFSftimes(revAdjDict, vertex, explored, ftimes, t):
    explored.add(vertex)
    if vertex in revAdjDict:
        for head in revAdjDict[vertex]:
            if head not in explored:
                t = DFSftimes(revAdjDict, head, explored, ftimes, t)
    t = t+1
    ftimes[vertex] = t
    global invFtimes
    invFtimes[t] = vertex
    return t


def DFSleaders(adjDict, ftimes, vertex, source, explored, leaders):
    if vertex in explored:
        return
    explored.add(vertex)
    leaders[vertex] = source
    origVertex = invFtimes[vertex]
    if origVertex in adjDict:
        for head in adjDict[origVertex]:
            head = ftimes[head]
            DFSleaders(adjDict, ftimes, head, source, explored, leaders)


def kosaraju(adjDict, revAdjDict, vertexSet):
    explored = set()
    ftimes = dict()
    t = 0
    verticeSet = set()
    for index, vertex in enumerate(list(sorted(vertexSet, reverse=True))):
        if vertex not in explored:
            t = DFSftimes(revAdjDict, vertex, explored, ftimes, t)
    explored = set()
    leaders = dict()

    for index, vertex in enumerate(range(t, 0, -1)):
        if vertex not in explored:
            DFSleaders(adjDict, ftimes, vertex, vertex, explored, leaders)
    return leaders, ftimes


def origLeaders(leaders, invFtimes):
    origLeaders = {}
    for key, val in leaders.items():
        origLeaders[invFtimes[key]] = invFtimes[val]
    return origLeaders

filename = "2sat1.txt"
edgeList = createEdgeList(filename)
adjDict, revAdjDict, vertexSet = createAdjDict(edgeList)
leaders = kosaraju(adjDict, revAdjDict, vertexSet)
numScc = len(leaders)
print("Found {} connected components".format(numScc))
