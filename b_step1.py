def heap_push(arr, x):
    arr.append(x)

    now_node = len(arr)-1

    while now_node > 0:
        parent_node = (now_node - 1)//2
        if arr[now_node][1] <= arr[parent_node][1]:
            arr[now_node], arr[parent_node] = arr[parent_node], arr[now_node]
            now_node = parent_node
        else:
            break

    return arr

n, m , s= map(int, input().split())

s -= 1

g = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    g[a] = heap_push(g[a], [b, w])

print(g[s][0][0]+1)

#for gi in g:
#    print(gi)