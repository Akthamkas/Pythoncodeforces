s = int(input())
t = list(input().lower())
letters = ['abcdefghijklmnopqrstuvwxyz']
counter = 0
for j in t:
    if j in letters:
        print("YES")
        break
    else:
        print("NO")
        break