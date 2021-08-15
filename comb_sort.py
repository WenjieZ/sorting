# Comb Sort

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a)

k = 1.3
g = int(len(a) / k)
while int(g) > 1:
    for i in range(len(a)-g):
        if a[i] > a[i+g]:
            a[i], a[i+g] = a[i+g], a[i]
    print(a, f'gap={g}')
    g = int(g / k)
            
for i in range(len(a)-1, 0, -1):
    is_sorted = True
    for j in range(i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            is_sorted = False
    if is_sorted:
        break
    print(a, f'gap={g}')