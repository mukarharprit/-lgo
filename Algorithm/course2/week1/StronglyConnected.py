def DFS(edgeList, vertex, explored, ftimes, t):
    explored.add(vertex)
    for (tail, head) in edgeList:
        if head == vertex and tail not in explored:
            t = DFS(edgeList, tail, explored, ftimes, t)
    t = t+1
    ftimes[vertex] = t
    return t

def DFSRound2(edgeList, ftimes, vertex, source, explored, leaders):
    explored.add(vertex)
    leaders[vertex] = source
    for (tail, head) in edgeList:
        tailA = ftimes[tail]
        headA = ftimes[head]
        if tailA == vertex and headA not in explored:
            DFSRound2(edgeList, ftimes, headA, source, explored, leaders)

def StronglyConnectedComponent(filename):
    f = open(filename)
    edgeList = [ (int(line.split()[0]), int(line.split()[1])) for line in f ]
    exploredVertex = set()
    ftimes = dict()
    t = 0
    verticeSet = set()
    for (tail, head) in edgeList:
        verticeSet.add(head)
        verticeSet.add(tail)
    for vertex in range(max(verticeSet), min(verticeSet)-1, -1):
        if vertex not in exploredVertex:
            t = DFS(edgeList, vertex, exploredVertex, ftimes, t)
    exploredVertex = set()
    leaders = dict()
    for vertex in range(t, 0, -1):
        if vertex not in exploredVertex:
            DFSRound2(edgeList, ftimes, vertex, vertex, exploredVertex, leaders)
    return leaders


head = StronglyConnectedComponent("SCC.txt")
print("Found {} connected components".format(len(set(head.values()))))
