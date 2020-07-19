s = list(map(int,input().split()))
li = []
count = 0
for j in s:
    if j not in li:
        li.append(j)
    else:
        count+=1
print(count)