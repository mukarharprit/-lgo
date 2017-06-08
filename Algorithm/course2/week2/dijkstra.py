import operator
import random
class dijkstra:
    def readGraph(self,filename):
        graph = []
        with open(filename) as file:
            for line in file.readlines():
                a = line.split()
                a = [list(map(int,x.split(','))) for x in a]
                graph.append(a)
        return graph
    def dijkstraMin(self,filename):
        graph = self.readGraph(filename)
        cost = {}

        for i in range(1,201):
            cost[i] = int(str(i) + "9999999999")
        cost[1] = 0
        visited = set()
        visited.add(1)
       # print (visited)
        for vert in graph:
            flag = 1
            u = 0
            for vw in vert:
                if flag == 1:
                    flag = 0
                    u = visited.pop()
                    continue
                v = vw[0]
                visited.add(v)
                cost[v] = min(cost[v],cost[u] + vw[1])
        sorted_cost = sorted(cost.items(), key=operator.itemgetter(1))
        return sorted_cost[:10]

obj = dijkstra()
cost10 = obj.dijkstraMin("dijkstraData.txt")
print (cost10)

