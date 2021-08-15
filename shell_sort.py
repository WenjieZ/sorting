# Shell Sort

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a)

gaps = [5, 3, 1]
for g in gaps:
    for k in range(g):
        for i in range(k+g, len(a), g):
            temp = a[i]
            j = i - g
            while j >=0 and a[j] > temp:
                a[j+g] = a[j]
                j -= g
            a[j+g] = temp
    print(a)