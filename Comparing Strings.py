a = input()
b = input()
for k,j in zip(a,b[::-1]):
    if k==j:
        print("YES")
        break
    else:
        print('NO')
        break