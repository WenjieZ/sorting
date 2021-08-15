# Counting Sort

a = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a)

count = [0] * (max(a)+1)
for k in a:
    count[k] += 1
    
for i in range(len(count)-1):
    count[i+1] += count[i]
    
b = [0] * len(a)
for k in reversed(a):
    count[k] -= 1
    b[count[k]] = k
print(b)