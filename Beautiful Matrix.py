a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))
a3 = list(map(int, input().split()))
a4 = list(map(int, input().split()))
a5 = list(map(int, input().split()))
m = []
m.append(a1)
m.append(a2)
m.append(a3)
m.append(a4)
m.append(a5)
row = col = -1
for i in range(5):
    for j in range(5):
        if m[i][j] == 1:
            row = i
            col = j
            break
    if row != -1 and col != -1:
        break
r = abs(row - 2)
c = abs(col - 2)
print(r + c)