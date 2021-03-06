import random

def readEdges():
    edges = []
    with open('kargerMinCut.txt', 'r') as f:
        for l in f.readlines():
            nodeLine = list(map(int, l.split()))
            fst = nodeLine[0]
            for snd in nodeLine[1:]:
                if (snd, fst) not in edges:
                    edges.append((fst, snd))
    return edges

def minCut(edges):
    while vertexes(edges) > 2:
        edg = random.choice(edges)
        edges.remove(edg)
        for u,v in list(edges):
            if u==edg[1]:
                edges.remove((u,v))
                edges.append((edg[0],v))
            if v==edg[1]:
                edges.remove((u,v))
                edges.append((u,edg[0]))

        for u,v in list(edges):
            if u==v:
                edges.remove((u,v))
    print (str(len(edges))+"\n")
    return len(edges)

def vertexes(edges):
    v = set((f,s) for f,s in edges)
    return len(v)




e = readEdges()
r = [minCut(list(e)) for i in range(0, 2)]
print ("\nMin: " + str(min(r)))
