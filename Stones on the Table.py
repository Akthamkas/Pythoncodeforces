n = int(input())
s = input()
counter = 0
for j in range(1,len(s)):
    if s[j]==s[j-1]:
        counter+=1
    else:
        counter+=0
print(counter)