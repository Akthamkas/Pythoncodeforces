t = int(input())
li = []
for k in range(t):
    x,y,n = map(int,input().split())
    for j in range(1,n+1):
        if n//j==y%x:
            li.append(j)
print(max(li))