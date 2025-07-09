for i in range(5):
    print(i, end=' ')
    if i==2:
        break
else :
    print('Success with break')

for j in range(5):
    print(j, end='\n')
else:
    print('Success without break')

# to perform the else bloc we need to finish naturally the while bloc , do a break doesn't execute the else bloc