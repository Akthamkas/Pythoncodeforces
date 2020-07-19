for x in range(int(input())):
    a = input()
    print(a if len(a)<11 else (str(a[0])+str(len(a[1:-1]))+str(a[-1])))