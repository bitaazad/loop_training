A=int(input('enter a number: '))
if A<=5:
    while A<=5: 
         A=int(input('enter a number again: '))
    else:
        if A>5:
            while A>5:
             print("the last number you entered was",A )
             break
elif A>5:
     while A>5:
        print("the last number you entered was",A )
        break
