n = 10
arr = [[1 - (i % 2) for k in range(n)] for i in range(n)]
for r in arr:
    print(*r)
