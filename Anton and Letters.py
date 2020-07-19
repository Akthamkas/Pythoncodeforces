s = (map(str,input().split("{,}")))
d = set()
count = 0
for k in s:
    if k not in d:
        d.update(k)
        count+=1
print(count)