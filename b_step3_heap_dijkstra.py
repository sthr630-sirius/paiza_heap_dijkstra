def heap_pop(bi_tree):
    bi_tree[0] = bi_tree[len(bi_tree)-1]
    bi_tree.pop()

    current_node = 0

    child_node_left = 2*current_node+1
    child_node_right = 2*current_node+2

    while child_node_left < len(bi_tree):
        if child_node_right >= len(bi_tree):
            target_node = child_node_left
        elif bi_tree[child_node_left][1] < bi_tree[child_node_right][1]:
            target_node = child_node_left
        elif bi_tree[child_node_left][1] == bi_tree[child_node_right][1]:
            if bi_tree[child_node_left][0] < bi_tree[child_node_right][0]:
                target_node = child_node_left
            else:
                target_node = child_node_right
        else:
            target_node = child_node_right

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

def heap_append(bi_tree, b, w):
    bi_tree.append([b, w])
    current_node = len(bi_tree) - 1

    #print(f"add element: {bi_tree[current_node]}")

    while current_node > 0:
        if current_node%2 == 0:
            parent_node = (current_node-2) // 2
        else:
            parent_node = (current_node-1) // 2

        #print(f"parent_node: {parent_node}")
        #print(f"parent_node element: {bi_tree[parent_node]}")

        if bi_tree[current_node][1] < bi_tree[parent_node][1]:
            bi_tree[current_node], bi_tree[parent_node] = bi_tree[parent_node], bi_tree[current_node]
            current_node = parent_node
        elif bi_tree[current_node][1] == bi_tree[parent_node][1]:
            if bi_tree[current_node][0] < bi_tree[parent_node][0]:
                bi_tree[current_node], bi_tree[parent_node] = bi_tree[parent_node], bi_tree[current_node]
                current_node = parent_node
            else:
                break
        else:
            break

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
bi_tree = []

nxt_node = s
heap_append(bi_tree, nxt_node, 0)
dist[nxt_node] = 0
is_visited[nxt_node] = True
#print(f"init bi_tree: {bi_tree}")

while not all(is_visited):
    now_node = nxt_node
    #print(f"---now_node: {now_node}")

    for node, w in g[now_node]:
        if is_visited[node] == False:
            #print(f"  now_node: {now_node}, append_node: {node}, path: {path+w}")
            heap_append(bi_tree, node, path+w)
    #print(f"added bi_tree: {bi_tree}")

    heap_pop(bi_tree)
    #print(f"poped bi_tree: {bi_tree}")
    if not bi_tree:
        break
    nxt_node = bi_tree[0][0]
    path = bi_tree[0][1]
    #print(nxt_node)
    #print(path)

    while is_visited[nxt_node]:
        if not bi_tree:
            break
        heap_pop(bi_tree)
        nxt_node = bi_tree[0][0]
        path = bi_tree[0][1]

    is_visited[nxt_node] = True
    dist[nxt_node] = path

    print(nxt_node+1)
    #print(f"nxt_node: {nxt_node}")
    #print(f"dist: {dist}")
    #print(f"is_visited: {is_visited}")

for d in dist:
    if d == INF:
        print('inf')
    else:
        print(d)
#print(is_visited)
