n,h = map(int,input().split())
counter = 0
a = map(int,input().split())
for j in a:
    if j<=h:
        counter+=1
    else:
        counter+=2
print(counter)