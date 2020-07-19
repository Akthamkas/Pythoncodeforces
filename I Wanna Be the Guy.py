n=int(input())
a=input().split()[1:]
b=input().split()[1:]
c=set(a+b)
if len(c)==n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")