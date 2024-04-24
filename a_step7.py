def heap_push(arr, x):
    arr.append(x)
    now_node = len(arr)-1
    while now_node > 0:
        parent_node = (now_node-1) // 2
        if arr[parent_node] > arr[now_node]:
            arr[parent_node], arr[now_node] = arr[now_node], arr[parent_node]
            now_node = parent_node
        else:
            break

    return arr

def heap_pop(arr):
    print(arr.pop(0))

    if len(arr) == 0:
        return arr

    arr = [arr.pop()] + arr
    now_node = 0
    while now_node <= len(arr):
        child_node1 = 2*now_node + 1
        child_node2 = 2*now_node + 2

        if child_node1 > len(arr)-1:
            break

        elif child_node2 > len(arr)-1:
            if arr[now_node] > arr[child_node1]:
                arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                now_node = child_node1
            else:
                break

        elif child_node2 <= len(arr)-1:
            if arr[child_node1] <= arr[child_node2]:
                if arr[now_node] > arr[child_node1]:
                    arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                    now_node = child_node1
                else:
                    break
            else:
                if arr[now_node] > arr[child_node2]:
                    arr[now_node], arr[child_node2] = arr[child_node2], arr[now_node]
                    now_node = child_node2
                else:
                    break

    return arr

n, q = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(q):
    query = list(input().split())
    if len(query) == 1:
        a = heap_pop(a)
    elif len(query) == 2:
        a = heap_push(a, int(query[1]))

print(*a)