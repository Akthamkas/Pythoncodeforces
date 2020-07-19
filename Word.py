s = input()
capCounter = 0
smallCounter = 0
cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #Capital letters
small = 'abcdefghijklmnopqrstuvwxyz' #small letters
for x in s:
    if x in cap:
        capCounter+=1
    elif x in small:
        smallCounter+=1
if capCounter>smallCounter:
    print(s.upper())
else:
    print(s.lower())