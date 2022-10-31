'''This is to demonstrate the looping with python,
compare the code and the output, you should see the logic behind'''

  
    
x=list(range(1,11))
for i in x:
    if i>7:
        print(i,'is larger than 7')

x=list(range(1,11))
for i in x:
    if i>7:
        break
    print(i)

x=list(range(1,11))
for i in x:
    if i>7:
        print(i,'is larger than 7')
    else:
        print(i,'is <= 7')
        
x=list(range(1,11))
for i in x:
    if i>7:
        break
        print(i,'is larger than 7')
    else:
        print(i,'is <= 7')

x=list(range(10,21))
for i in x:
    if i%2==0:
        print('2 is divider of',i)
    if i%3==0:
        print('3 is divider of',i)
    else:
        print('2 & 3 is not divider of',i)

     
x=list(range(10,21))
for i in x:
    if i%2==0:
        print('2 is divider of',i)
    elif i%3==0:
        print('3 is divider of',i)
    else:
        print('2 & 3 is not divider of',i)
