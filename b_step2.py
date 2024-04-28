def heap_push(arr):
    now_node = len(arr)-1
    while now_node > 0:
        parent_node = (now_node - 1) // 2
        if (step[arr[now_node]] < step[arr[parent_node]]) or ((step[arr[now_node]] == step[arr[parent_node]]) and (arr[now_node] < arr[parent_node])):
            arr[now_node], arr[parent_node] = arr[parent_node], arr[now_node]
            now_node, parent_node = parent_node, now_node
            position[arr[now_node]] = now_node
            position[arr[parent_node]] = parent_node
        else:
            break

def swap(arr, idx):
    now_node = idx
    while now_node > 0:
        parent_node = (now_node - 1) // 2
        #print(now_node)
        #print(parent_node)
        #print(arr)
        #print(arr[now_node])
        #print(step[arr[now_node]])
        if (step[arr[now_node]] < step[arr[parent_node]]) or ((step[arr[now_node]] == step[arr[parent_node]]) and (arr[now_node] < arr[parent_node])):
            arr[now_node], arr[parent_node] = arr[parent_node], arr[now_node]
            now_node, parent_node = parent_node, now_node
            position[arr[now_node]] = now_node
            position[arr[parent_node]] = parent_node
        else:
            break
def heap_pop(arr):
    node = arr.pop(0)

    if len(arr) == 0:
        return arr, node

    arr = [arr.pop()] + arr

    now_node = 0
    while now_node < len(arr):
        child_node1 = 2 * now_node + 1
        child_node2 = 2 * now_node + 2
        if child_node1 > len(arr) - 1:
            break
        if child_node2 > len(arr) - 1:
            if ((step[arr[now_node]] > step[arr[child_node1]]) or  ((step[arr[now_node]] == step[arr[child_node1]]) and (arr[now_node] > arr[child_node1]))):
                arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                now_node, child_node1 = child_node1, now_node
                position[arr[now_node]] = now_node
                position[arr[child_node1]] = child_node1
            else:
                break
        if child_node2 <= len(arr) - 1:
            if ((step[arr[child_node1]] < step[arr[child_node2]]) or ((step[arr[child_node1]] == step[arr[child_node2]]) and (arr[child_node1] < arr[child_node2]))):
                if ((step[arr[now_node]] > step[arr[child_node1]]) or  ((step[arr[now_node]] == step[arr[child_node1]]) and (arr[now_node] > arr[child_node1]))):
                    arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                    now_node, child_node1 = child_node1, now_node
                    position[arr[now_node]] = now_node
                    position[arr[child_node1]] = child_node1
                else:
                    break
            else:
                if ((step[arr[now_node]] > step[arr[child_node2]]) or  ((step[arr[now_node]] == step[arr[child_node2]]) and (arr[now_node] > arr[child_node2]))):
                    arr[now_node], arr[child_node2] = arr[child_node2], arr[now_node]
                    now_node, child_node2 = child_node2, now_node
                    position[arr[now_node]] = now_node
                    position[arr[child_node2]] = child_node2
                else:
                    break
    return arr, node

n, m, s = map(int, input().split())
s -= 1
inf = 100100100100

g = [[] for _ in range(n)]

step = [inf]*n
position = [inf]*n
is_visited = [False]*n
adj_nodes = []
path = []

for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, w])
    g[a] = sorted(g[a])

#print(g[2])

# スタート
now_v = s
step[now_v] = 0
is_visited[now_v] = True
path.append(now_v+1)

now_step = step[now_v]

for i in range(2):
    # 隣接nodeをリストに追加、最短nodeを先頭にソート
    for i in range(len(g[now_v])):
        adj_node = g[now_v][i][0]
        if not is_visited[adj_node]:
            if position[adj_node] == inf:
                adj_nodes.append(adj_node)
                step[adj_node] = min(step[adj_node], g[now_v][i][1] + now_step)
                position[adj_node] = len(adj_nodes)-1

                heap_push(adj_nodes)

                #print(f"adj:{adj_nodes}")
                #print(f"step:{step}")
                #print(f"position:{position}")
                #print(f"is_visited:{is_visited}")
                #print("----------------")

            else:
                step[adj_node] = min(step[adj_node], g[now_v][i][1] + now_step)
                if len(adj_nodes) > 1:
                    swap(adj_nodes, position[adj_node])

    #print(f"adj:{adj_nodes}")
    #print(f"step:{step}")
    #print(f"position:{position}")
    #print(f"is_visited:{is_visited}")

    if not adj_nodes:
        break

    # 最短nodeを取得、最短nodeへ移動、pathに追加
    adj_nodes, now_v = heap_pop(adj_nodes)
    is_visited[now_v] = True
    path.append(now_v+1)

    #print("----pop-------")
    #print(f"adj:{adj_nodes}")
    #print(f"step:{step}")
    #print(f"position:{position}")
    #print(f"is_visited:{is_visited}")

    # 初期nodeから現在nodeまでのstep
    now_step = step[now_v]

for i in range(1, 3):
    if i < len(path):
        print(path[i])
    else:
        print("inf")