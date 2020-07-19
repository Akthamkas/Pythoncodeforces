num1 = input()
num2 = input()
li = []
for k,j in zip(num1,num2):
    if k!=j:
        li.append('1')
    else:
        li.append('0')
print(''.join(li))