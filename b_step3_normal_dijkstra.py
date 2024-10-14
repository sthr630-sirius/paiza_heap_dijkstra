n, m, s = map(int, input().split())
s -= 1
g = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, w])

INF = 2 * 1000

is_visited = [False]*n
dist = [INF]*n
path = 0
nxt_nodes = []

nxt_node = s
dist[nxt_node] = 0
is_visited[nxt_node] = True
#nxt_nodes.append([nxt_node, 0])

while not all(is_visited):
    now_node = nxt_node
    path = dist[now_node]
    # update adjacent node
    for nxt_node, w in g[now_node]:
        if path + w < dist[nxt_node]:
            dist[nxt_node] = path + w

    # get node of min dist
    min_dist = INF
    min_node = 1000
    for node in range(n):
        if not is_visited[node]:
            if dist[node] < min_dist:
                min_dist = dist[node]
                min_node = node
            elif dist[node] == min_dist:
                min_node = min(min_node, node)

    nxt_node = min_node
    is_visited[nxt_node] = True

    if min_dist != INF:
        print(nxt_node+1)

for d in dist:
    if d == INF:
        print('inf')
    else:
        print(d)