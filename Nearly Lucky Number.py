n = int(input())
counter = 0
while n>0:
    d = n%10
    if d==7 or d==4:
        counter+=1
    n = n//10
if counter==7 or counter==4:
    print("YES")
else:
    print("NO") 