def cluster(NoOfClust, desiredClustNo, sorted_edges, Nodes):
    while NoOfClust > desiredClustNo:
        A, B, edge_dist = sorted_edges.pop(0)
        while Sroot(A, B, Nodes): 
            A, B, edge_dist = sorted_edges.pop(0)
        union(A, B, Nodes)
        NoOfClust -= 1
    A, B, edge_dist = sorted_edges.pop(0)
    while Sroot(A, B, Nodes): 
        A, B, edge_dist = sorted_edges.pop(0)
    return A, B, edge_dist


def Sroot(A, B, Nodes):
    a_root = findNodeSet(A, Nodes)
    b_root = findNodeSet(B, Nodes)
    return a_root == b_root

def union(A, B, Nodes):
    a_root = findNodeSet(A, Nodes)
    b_root = findNodeSet(B, Nodes)
    link(a_root, b_root, Nodes)


def link(node_x, node_y, Nodes):
    if Nodes[node_x][1] > Nodes[node_y][1]:
        Nodes[node_y][0] = node_x
    else:
        Nodes[node_x][0] = node_y
        if Nodes[node_x][1] == Nodes[node_y][1]:
            Nodes[node_y][1] += 1


def findNodeSet(node, Nodes):
    if node != Nodes[node][0]:
        Nodes[node][0] = findNodeSet(Nodes[node][0], Nodes)
    return Nodes[node][0]


def main():
    edges = []
    with open('clustering1.txt') as file_in:
        next(file_in)
        for line in file_in:
            edges.append(list(map(int, line.split(' '))))
    sorted_edges = sorted(edges, key = lambda edge: edge[-1])
    NoOfClust = int(open('clustering1.txt').readline().strip())
    desiredClustNo = 4
    Nodes = dict([[i, [i, 0]] for i in range(1, NoOfClust + 1)]) 
    return cluster(NoOfClust, desiredClustNo, sorted_edges, Nodes)

print( main())
