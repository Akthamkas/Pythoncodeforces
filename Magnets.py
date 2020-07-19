n = int(input())
i = ''
for k in range(n):
    i+= input()
print(i.count('00')+i.count('11')+1)