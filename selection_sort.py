# Selection Sort

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a)

for i in range(len(a)-1):
    p = i
    for j in range(i+1, len(a)):
        if a[j] < a[p]:
            p = j
    if p != i:
        a[i], a[p] = a[p], a[i]
        
print(a)