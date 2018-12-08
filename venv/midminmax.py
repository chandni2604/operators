a=float(input('enter val of a'))
b=float(input('enter val of b'))
c=float(input('enter val of c'))
if(a==b and b==c):
    print("a=b=c both same")

elif(a<b<c or a<c<b):
    print('min=',a)
elif(b<a<c or b<c<a):
    print('min=',b)
else:
    print('min=', c)
if(a>b>c or a>c>b):
print('max=',a)

elif(b>c>a or b>a>c):
    print('max=',b)
else:
    print('max=',c)
if(b<a<c or c<a<b):
    print('mid=',a)
elif(c<b<a or a<b<c):
    print('mid=',b)
else:
    print('mid=',c)

