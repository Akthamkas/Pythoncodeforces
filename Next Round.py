n,k = map(int,input().split())
a = list(map(int,input().split()))
x = a[k-1]
count = 0
for k in range(0,len(a)):
    if a[k]>=x and a[k]>0:
        count+=1
print(count)