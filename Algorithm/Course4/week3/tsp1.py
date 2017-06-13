from itertools import chain, combinations
from math import sqrt
from sys import argv, maxint
import numpy as np


def load_graph(path):
  
  with open(path) as reader:
    n_nodes = int(reader.readline())
    nodes = [map(float, line.split()) for line in reader]
    return n_nodes, nodes


def distance(node_a, node_b):
  
  return sqrt((node_a[0] - node_b[0]) ** 2 + (node_a[1] - node_b[1]) ** 2)



def tsp2(points):
  
  all_distances = [[distance(x,y) for y in points] for x in points]
 
  A = {(frozenset([0, idx+1]), idx+1): (dist, [0,idx+1]) for idx,dist in enumerate(all_distances[0][1:])}
  cnt = len(points)
  for m in range(2, cnt):
  
    B = {}
    for S in [frozenset(C) | {0} for C in combinations(range(1, cnt), m)]:
      for j in S - {0}:
        B[(S, j)] = min((A[(S-{j},k)][0] + all_distances[k][j], A[(S-{j},k)][1] + [j]) for k in S if k != 0 and k!=j)
    A = B
  res = min([(A[d][0] + all_distances[0][d[1]]) for d in iter(A)])
  return res

def main():
 
  n_nodes, nodes = load_graph(argv[1])
 
  print tsp2(nodes)

if __name__ == '__main__':
  main()
