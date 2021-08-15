# Bubble Sort

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a)

for i in range(len(a)-1, 0, -1):
    is_sorted = True
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            is_sorted = False
    if is_sorted:
        break
    print(a)