n = int(input())
p = map(int,input().split())
counter = 0
for k in p:
    counter+=k
print(counter/n)