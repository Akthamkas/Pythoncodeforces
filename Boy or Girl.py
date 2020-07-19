s = input()
li = []
counter = 0
for k in s:
    if k not in li:
        li.append(k)
        counter+=1

if counter%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")