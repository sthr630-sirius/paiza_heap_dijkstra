a = list(map(int, input().split()))
a[0] = a[len(a)-1]
a.pop()

current_node_idx = 0
child_node_left = 2*current_node_idx + 1
child_node_right = 2*current_node_idx + 2

while child_node_left < len(a):
    if(a[child_node_left] <= a[child_node_right]):
        target_node_idx = child_node_left
    else:
        target_node_idx = child_node_right

    if(a[current_node_idx] > a[target_node_idx]):
        a[current_node_idx], a[target_node_idx] = a[target_node_idx], a[current_node_idx]
        current_node_idx = target_node_idx
        child_node_left = 2 * current_node_idx + 1
        child_node_right = 2 * current_node_idx + 2
    else:
        break

print(*a)