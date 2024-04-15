from collections import deque

n = int(input())
parent = [-1]*(2*n)

nxt_vertices = deque()

nxt_v = 0
nxt_vertices.append(nxt_v)

while nxt_v < n:
    now_v = nxt_vertices.popleft()
    for i in range(1, 3):
        nxt_v = 2*now_v + i
        nxt_vertices.append(nxt_v)
        parent[nxt_v] = now_v
        #print(f"p:{now_v}")
        #print(f"c:{nxt_v}")

#print(parent)
print(parent[n])