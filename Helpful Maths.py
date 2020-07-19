math = input()
math = list(math)
for j in math:
    if j=='+':
        math.remove(j)
print('+'.join(sorted(math)))