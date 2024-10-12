a = list(map(int, input().split()))
x = int(input())
a.append(x)
current_node = len(a)-1

while current_node != 0:
    if current_node%2 == 0:
        parent_node = (current_node-2) // 2
    else:
        parent_node = (current_node-1) // 2

    if(a[current_node] <= a[parent_node]):
        a[current_node], a[parent_node] = a[parent_node], a[current_node]
        current_node = parent_node
    else:
        break

print(*a)
