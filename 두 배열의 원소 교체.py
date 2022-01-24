a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]

for k in range(3):
    min_a = min(a)
    max_b = max(b)
    for i in range(len(a)):
        if a[i] == min_a:
            ai = i
            break
    for j in range(len(b)):
        if b[j] == max_b:
            bi = j
            break
            
    a[ai], b[bi] = b[bi], a[ai]

print(sum(a), sum(b))