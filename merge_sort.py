# Merge Sort

def merge(a, b):
    c = []
    while a and b:
        if a[0] <= b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
    if a:
        c.extend(a)
    else:
        c.extend(b)
    return c

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a)

length = 1
while length < len(a):
    for i in range(0, len(a), 2*length):
        a[i:min(len(a), i+2*length)] = merge(a[i:min(len(a), i+length)], a[i+length:min(len(a), i+2*length)])
    length *= 2    
print(a)