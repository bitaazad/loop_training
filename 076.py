A=int(input('enter a number between 10 and 20: '))
if A<10:
 while A<10:
     print('too low')  
     A=int(input('enter a number between 10 and 20 again: '))
 else:
     if A>20:
        while A>20:
          print('too high')  
          A=int(input('enter a number between 10 and 20 again: '))
        else:
            if A<10:
                while A<10:
                 print('too low')
                 A=int(input('enter a number between 10 and 20 again: '))  
            elif A>10 and A<20:
                 print('thank you')
if A>20:    
 while A>20:
     print('too high')
     A=int(input('enter a number between 10 and 20 again: '))
 else:
     if A<10:
        while A<10:
          print('too low')  
          A=int(input('enter a number between 10 and 20 again: '))
        else:
            if A>20:
             while A>20:
              print('too high')
              A=int(input('enter a number between 10 and 20 again: '))  
            elif A>10 and A<20:
                 print('thank you')
     
     else:
         print('thank you')
else:
    print('thank you')