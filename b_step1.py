n, m, s = map(int, input().split())
s -= 1
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, w])

near_edge = 'inf'
min_w = 11

for gi in g[s]:
    edge = gi[0]
    w = gi[1]
    if w < min_w:
        min_w = w
        near_edge = edge
    elif w == min_w:
        near_edge = min(near_edge, edge)

if near_edge != 'inf':
    print(near_edge+1)
else:
    print('inf')