n = int(input())
c =m= 0
for k in range(n):
    a,b = map(int, input().split())
    c-=a
    c+=b
    m = max(m,c)
print(m)
