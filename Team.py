n = int(input())
counter = 0
while n>0:
    q = list(map(str,input()))
    n-=1
    x = q.count('1')
    if x>=2:
        counter+=1
    else:
        counter+=0
print(counter)