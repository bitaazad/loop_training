l1=[]
A=input('do yo want to enter a number: ')
while A=='yes':
    B=int(input('enter a number: '))
    l1.append(B)
    print(*l1)
    A=input('do yo want to enter a number: ')
else:
    print(*l1)
