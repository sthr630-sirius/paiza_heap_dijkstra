def heap_push(arr, arr_g, previous_w):
    for i in range(len(arr_g)):
        arr_g[i][1] += previous_w
        arr.append(arr_g[i])

        now_node = len(arr)-1

        while now_node > 0:
            parent_node = (now_node-1)//2
            if arr[now_node][1] < arr[parent_node][1]:
                arr[now_node], arr[parent_node] = arr[parent_node], arr[now_node]
                now_node = parent_node
            else:
                 break

    return arr


n, m, s = map(int, input().split())

s -= 1

g = [[] for _ in range(n)]

near_node = []
shortest_path = []

for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append([b, w])

previous_w = 3
start_node = s

#near_node = heap_push(near_node, g[start_node])
near_node = heap_push(near_node, g[4], previous_w)


print("----")
print(near_node)
print("----")

for gi in g:
    print(gi)