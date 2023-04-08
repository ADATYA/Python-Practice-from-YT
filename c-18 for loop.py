                   ###   for loop with range()  ###

# range(start,condition,increment)
# Start 0
# condition < 5 (n-1)
# increment 1

# range is a pre-define function
# range 3 parameter obdi hote pare

for i in range(5):
    print(i)
print('\n\n')

for i in range(1,6):
    print(i)

print('\n\n')

for i in range(1,6,2):
    print(i)


# create a table :

print('\n\n')

for a in range(1,11):
    print('2 X',a,'=',2*a)

print('\n\n')

num=int(input("Enter a number :" ))

for i in range(1,11):
    print(num, 'X',i,'=',num*i)


                             ### Reverse ###

# range (Start,condition,increment(-1))

# range er last parameter e decrement thaka mandatory (-1)
print('\n\n')
for i in range(10,0,-1):
    print(i)
print('\n\n')

for i in range(10,0,-2):
    print(i)