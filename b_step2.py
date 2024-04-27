def heap_push(arr):
    now_node = len(arr)-1
    while now_node > 0:
        parent_node = (now_node - 1) // 2
        if step[arr[now_node]] <= step[arr[parent_node]]:
            arr[now_node], arr[parent_node] = arr[parent_node], arr[now_node]
            now_node = parent_node
        else:
            break
def heap_pop(arr):
    now_node = 0
    while now_node < len(arr):
        child_node1 = 2 * now_node + 1
        child_node2 = 2 * now_node + 2
        if child_node1 > len(arr) - 1:
            break
        if child_node2 > len(arr) - 1:
            if step[arr[now_node]] > step[arr[child_node1]]:
                arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                now_node = child_node1
            else:
                break
        if child_node2 <= len(arr) - 1:
            if step[arr[child_node1]] <= step[arr[child_node2]]:
                if step[arr[now_node]] > step[arr[child_node1]]:
                    arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                    now_node = child_node1
                else:
                    break
            else:
                if step[arr[now_node]] > step[arr[child_node2]]:
                    arr[now_node], arr[child_node2] = arr[child_node2], arr[now_node]
                    now_node = child_node2
                else:
                    break

n, m, s = map(int, input().split())
s -= 1
inf = 100100100100

g = [[] for _ in range(n)]

step = [inf]*n
is_visited = [False]*n
adj_nodes = []
path = []

for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, w])

now_v = s

step[now_v] = 0
is_visited[now_v] = True
path.append(now_v)

now_step = step[now_v]

# 隣接nodeをリストに追加、最短nodeを先頭にソート
for i in range(len(g[now_v])):
    adj_node = g[now_v][i][0]
    if not is_visited[adj_node]:
        adj_nodes.append(adj_node)
        step[adj_node] = min(step[adj_node], g[now_v][i][1] + now_step)

        heap_push(adj_nodes)

# 最短nodeを取得、最短nodeへ移動、pathに追加
now_v = adj_nodes.pop(0)
is_visited[now_v] = True
path.append(now_v)

# 初期nodeから現在nodeまでのstep
now_step = step[now_v]

# 最短nodeを先頭にソート
adj_nodes = [adj_nodes.pop()] + adj_nodes
heap_pop(adj_nodes)

for i in range(len(g[now_v])):
    adj_node = g[now_v][i][0]
    if not is_visited[adj_node]:
        adj_nodes.append(adj_node)
        step[adj_node] = min(step[adj_node], g[now_v][i][1] + now_step)

        heap_push(adj_nodes)


now_v = adj_nodes.pop(0)
is_visited[now_v] = True
path.append(now_v)

now_step = step[now_v]

adj_nodes = [adj_nodes.pop()] + adj_nodes
heap_pop(adj_nodes)

print(adj_nodes)
print(is_visited)
print(step)
print(path)

#near_node = heap_push(near_node, g[start_node])
#near_node = heap_push(near_node, g[4], previous_w)

#print("----")
#print(near_node)
#print("----")

#for gi in g:
#    print(gi)