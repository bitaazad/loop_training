compnum=50
A=int(input('enter a number: '))
guess=[]
while A>50:
        print('your guess is too high')
        A=int(input('try another guess: '))
        guess.append(A)
while A<50:
        print('your guess is too low')
        A=int(input('try another guess: '))
        guess.append(A)
else:
    print('well done! after', len(guess)+1 , 'attempts')
