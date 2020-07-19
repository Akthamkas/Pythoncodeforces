n = int(input())
counter = 0
for k in range(n):
    p,q = (map(int,input().split()))
    if p+2<=q :
        counter+=1
    else:
        counter+=0
print(counter)