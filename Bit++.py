val=0
for _ in range(int(input())):
	val+=1 if '+' in input() else -1
print(val)