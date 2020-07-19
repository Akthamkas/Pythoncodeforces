n, k = map(int,input().split())
counter = 0
persons = map(int,input().split())
for h in persons:
    if h+k<=5:
        counter+=1
print(int(counter/3))