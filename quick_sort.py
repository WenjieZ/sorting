# Quick Sort

def quicksort(a, begin, end):
    if begin >= end:
        return a
    
    i, j, p = begin, end, begin
    while i < j:
        if p == i:
            while a[i] < a[j]:
                j -= 1
            a[i], a[j] = a[j], a[i]
            p, i = j, i+1
        else:
            while a[i] < a[j]:
                i += 1
            a[i], a[j] = a[j], a[i]
            p, j = i, j-1
    
    quicksort(a, begin, p-1)
    quicksort(a, p+1, end)
    return a

quicksort([9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 8)