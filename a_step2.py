from collections import deque

n = int(input())
parent = [-1]*(2*n)
path = []

nxt_vertices = deque()

nxt_v = 0
nxt_vertices.append(nxt_v)

while nxt_v < n:
    now_v = nxt_vertices.popleft()
    for i in range(1, 3):
        nxt_v = 2*now_v + i
        nxt_vertices.append(nxt_v)
        parent[nxt_v] = now_v

parent_v = n

while parent_v != -1:
    parent_v = parent[parent_v]
    path.append(parent_v)

print(*path[:-1])


"""
other code

path = []
while n > 0:
    n = (n-1)//2
    path.append(n)

print(path)
"""