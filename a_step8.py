def heap_push(arr, word_arr, x, word):
    arr.append(x)
    word_arr.append(word)

    now_node = len(arr)-1
    while now_node > 0:
        parent_node = (now_node-1) // 2
        if arr[parent_node] > arr[now_node]:
            arr[parent_node], arr[now_node] = arr[now_node], arr[parent_node]
            word_arr[parent_node], word_arr[now_node] = word_arr[now_node], word_arr[parent_node]
            now_node = parent_node
        else:
            break

    return arr, word_arr

def heap_pop(arr, word_arr):
    arr.pop(0)
    print(word_arr.pop(0))

    if len(arr) == 0:
        return arr, word_arr

    arr = [arr.pop()] + arr
    word_arr = [word_arr.pop()] + word_arr

    now_node = 0
    while now_node <= len(arr):
        child_node1 = 2*now_node + 1
        child_node2 = 2*now_node + 2

        if child_node1 > len(arr)-1:
            break

        elif child_node2 > len(arr)-1:
            if arr[now_node] > arr[child_node1]:
                arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                word_arr[now_node], word_arr[child_node1] = word_arr[child_node1], word_arr[now_node]
                now_node = child_node1
            else:
                break

        elif child_node2 <= len(arr)-1:
            if arr[child_node1] <= arr[child_node2]:
                if arr[now_node] > arr[child_node1]:
                    arr[now_node], arr[child_node1] = arr[child_node1], arr[now_node]
                    word_arr[now_node], word_arr[child_node1] = word_arr[child_node1], word_arr[now_node]
                    now_node = child_node1
                else:
                    break
            else:
                if arr[now_node] > arr[child_node2]:
                    arr[now_node], arr[child_node2] = arr[child_node2], arr[now_node]
                    word_arr[now_node], word_arr[child_node2] = word_arr[child_node2], word_arr[now_node]
                    now_node = child_node2
                else:
                    break

    return arr, word_arr

n, q = map(int, input().split())
w = list(input().split())
a = list(map(int, input().split()))

for i in range(q):
    query = list(input().split())

    if query[0] == "pop":
        a, w = heap_pop(a, w)
    else:
        a, w = heap_push(a, w, int(query[2]), query[1])

print(*w)