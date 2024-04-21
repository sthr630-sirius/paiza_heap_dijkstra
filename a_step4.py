n = int(input())
a = list(map(int, input().split()))

x = int(input())
a.append(x)

target_idx = n

while target_idx > 0:
    parent_idx = (target_idx-1)//2

    if a[parent_idx] > a[target_idx]:
        a[parent_idx], a[target_idx] = a[target_idx], a[parent_idx]

    target_idx = parent_idx

print(*a)