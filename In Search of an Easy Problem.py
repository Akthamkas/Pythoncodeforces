n = int(input())
d = list(map(str,input()))
x = d.count('1')
if x>=1:
    print('HARD')
else:
    print('EASY')
