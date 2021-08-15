# Heap Sort

def heapify(a, floyd=False, bottom_up=False):
    if not floyd:
        for i in range(1, len(a)):
            siftup(a, i)
    else:
        for i in range(len(a)//2 - 1, -1, -1):
            siftdown(a, i, len(a), bottom_up)
    return a    
    
def siftup(a, i):
    while i > 0 and a[i] > a[(i-1)//2]:
        a[i], a[(i-1)//2] = a[(i-1)//2], a[i]
        i = (i-1) // 2
    return a
        
def siftdown(a, i, n, bottom_up=False):
    if not bottom_up:
        while (2*i+1 < n and a[i] < a[2*i+1]) or (2*i+2 < n and a[i] < a[2*i+2]):
            if 2*i+2 < n and a[2*i+1] < a[2*i+2]:
                a[i], a[2*i+2] = a[2*i+2], a[i]
                i = 2*i + 2
            else:
                a[i], a[2*i+1] = a[2*i+1], a[i]
                i = 2*i + 1
    else:
        j = i
        while 2*j+1 < n:
            if 2*j+2 < n and a[2*j+1] < a[2*j+2]:
                j = 2*j + 2
            else: 
                j = 2*j + 1
        
        while a[i] > a[j]:
            j = (j-1) // 2
        a[i], a[j] = a[j], a[i]
        while j > i:
            a[i], a[(j-1)//2] = a[(j-1)//2], a[i]
            j = (j-1) // 2
        
    return a
                
def heapsort(a, floyd=False, bottom_up=False):
    heapify(a, floyd, bottom_up)
    for i in range(len(a)-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        siftdown(a, 0, i, bottom_up)
    return a

heapsort([9, 8, 7, 6, 5, 4, 3, 2, 1], floyd=False, bottom_up=False)