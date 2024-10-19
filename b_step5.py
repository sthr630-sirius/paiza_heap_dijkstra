def heap_pop(bi_tree):
    bi_tree[0] = bi_tree[-1]
    bi_tree.pop()

    current_node = 0
    child_node_left = 2*current_node + 1
    child_node_right = 2*current_node + 2

    while child_node_left < len(bi_tree):
        if child_node_right < len(bi_tree):
            if bi_tree[child_node_left][1] < bi_tree[child_node_right][1]:
                target_node = child_node_left
            elif bi_tree[child_node_left][1] == bi_tree[child_node_right][1]:
                if bi_tree[child_node_left][0] < bi_tree[child_node_right][0]:
                    target_node = child_node_left
                else:
                    target_node = child_node_right
            else:
                target_node = child_node_right
        else:
            target_node = child_node_left

        if bi_tree[current_node][1] > bi_tree[target_node][1]:
            bi_tree[current_node], bi_tree[target_node] = bi_tree[target_node], bi_tree[current_node]
        elif bi_tree[current_node][1] == bi_tree[target_node][1]:
            if bi_tree[current_node][0] > bi_tree[target_node][0]:
                bi_tree[current_node], bi_tree[target_node] = bi_tree[target_node], bi_tree[current_node]
            else:
                break
        else:
            break

        current_node = target_node
        child_node_left = 2 * current_node + 1
        child_node_right = 2 * current_node + 2

def heap_push(bi_tree, b, w, v):
    bi_tree.append([b, w, v])

    current_node = len(bi_tree)-1

    while current_node > 0:
        if current_node % 2 == 0:
            parent_node = (current_node - 2) // 2
        else:
            parent_node = (current_node - 1) // 2

        if bi_tree[current_node][1] < bi_tree[parent_node][1]:
            bi_tree[current_node], bi_tree[parent_node] = bi_tree[parent_node], bi_tree[current_node]
        elif bi_tree[current_node][1] == bi_tree[parent_node][1]:
            if bi_tree[current_node][0] < bi_tree[parent_node][0]:
                bi_tree[current_node], bi_tree[parent_node] = bi_tree[parent_node], bi_tree[current_node]
            else:
                break
        else:
            break
        current_node = parent_node

INF = 1000

n, m, s, t, e = map(int, input().split())
s -= 1
t -= 1
e -= 1

bi_tree = []
g = [[] for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, w])

path_st = []
path_tg = []
dist_st = 0
dist_tg = 0
is_reachable = True

# s ----> t
is_visited = [False]*n
dist = [INF]*n
prev_node = [-1]*n

nxt_node = s
bi_tree.append([nxt_node, 0, -1])

while bi_tree:
    now_node = bi_tree[0][0]
    now_dist = bi_tree[0][1]
    prev = bi_tree[0][2]

    if not is_visited[now_node]:
        is_visited[now_node] = True
        dist[now_node] = now_dist
        prev_node[now_node] = prev
        heap_pop(bi_tree)

        for b, w in g[now_node]:
            prev = now_node
            heap_push(bi_tree, b, w+now_dist, prev)
    else:
        heap_pop(bi_tree)

if is_visited[t]:
    dist_st = dist[t]
    path_st.insert(0, t+1)
    prev = prev_node[t]
    while prev != -1:
        path_st.insert(0, prev+1)
        prev = prev_node[prev]
else:
    is_reachable = False

# t ----> g
is_visited = [False]*n
dist = [INF]*n
prev_node = [-1]*n

nxt_node = t
bi_tree.append([nxt_node, 0, -1])

while bi_tree:
    now_node = bi_tree[0][0]
    now_dist = bi_tree[0][1]
    prev = bi_tree[0][2]

    if not is_visited[now_node]:
        is_visited[now_node] = True
        dist[now_node] = now_dist
        prev_node[now_node] = prev
        heap_pop(bi_tree)

        for b, w in g[now_node]:
            prev = now_node
            heap_push(bi_tree, b, w+now_dist, prev)
    else:
        heap_pop(bi_tree)

if is_visited[e]:
    dist_tg = dist[e]
    path_tg.insert(0, e+1)
    prev = prev_node[e]
    while prev != -1:
        path_tg.insert(0, prev+1)
        prev = prev_node[prev]
else:
    is_reachable = False

# output s ---> t ---> g
if is_reachable:
    path = path_st + path_tg[1:]
    print(dist_st+dist_tg)
    print(*path)
else:
    print('inf')