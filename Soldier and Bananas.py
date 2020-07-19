k,n,w = map(int,input().split())
summ = 0
for j in range(0,w+1):
    summ+=j
z = (summ*k)-n
if z<0:
    print(0)
else:
    print(z)