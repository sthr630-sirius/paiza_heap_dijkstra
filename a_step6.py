n = int(input())
a = list(map(int, input().split()))

a.pop(0)
a = [a.pop()] + a

current_node = 0

while current_node <= n//2-1:
    child_node1 = 2 * current_node + 1
    child_node2 = 2 * current_node + 2
    # 葉は何もしない
    if child_node1 > n-1:
        break

    # 子が1つ
    if child_node2  > n-1:
        if a[current_node] > a[child_node1]:
            a[current_node], a[child_node1] = a[child_node1], a[current_node]
            current_node = child_node1
        continue

    #子が2つ
    if a[child_node1] <= a[child_node2]:
        if a[current_node] > a[child_node1]:
            a[current_node], a[child_node1] = a[child_node1], a[current_node]
            current_node  = child_node1
        else:
            break
    else:
        if a[current_node] > a[child_node2]:
            a[current_node], a[child_node2] = a[child_node2], a[current_node]
            current_node = child_node2
        else:
            break
print(*a)