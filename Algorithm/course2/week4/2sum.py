from lib.mergesort import mergesort
from lib.bisect import *

arr = []

with open('algo1_programming_prob_2sum.txt', 'r') as f:
    for line in f:
        arr.append(int(line.rstrip()))



A = mergesort(arr)

del arr



u = dict()

for i in xrange(-10000, 10001):
    u[i] = 0

for x in A:
    low_bound = -10000 - x
    upp_bound = 10000 - x

    left = bisect_left(A, low_bound)
    right = bisect_right(A, upp_bound)

    for y in xrange(left, right):
        if x == A[y]:
            continue

        t = x + A[y]

        u[t] = 1

print sum(u.itervalues())
