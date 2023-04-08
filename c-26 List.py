list=[1,2,3,4,[5,6,7],8,9,10] #Searching item 7 

# B=list.type()  #AttributeError: 'list' object has no attribute 'type'
# print(B)

print(type(list))

print(list.index(3))
# print(list.index(9)(7))  #TypeError: 'int' object is not callable
l=[1,2,3,[4,5,7]]
print(l[3][2])
print(l[3])
print(l[2])

# Mixed list system
l=[1,2,'bikrom',3]
print(l[-2])
print(l[2])

# List slicing

l=[7,1,'bikrom',[3,4,5,6]]
print(l[0:2]) #condition (n-1)
print(l[1:])
print(l[:])

list=[1,2,3,4,5,6,7]

#List slicing
print(list[0:6:2])
print(list[1:6:2])

#List reversing slicing
print(list[1:6])
print(list[-1::-1]) #condition dile[] faka list asche


                    # List Iteration ##
l=[10,20,30,70] 

t=len(l)
# for i in range:
print(t)

for i in range(t):
    print(l[i])

print('\n\n')

for i in l:
    print(i)


## Revers list ##

#   0  1  2  3  4  5
l=[10,20,30,50,60,90]   # n-1
#  -6 -5 -4 -3 -2 -1

f=len(l)
print(f)

print('\n')

for i in range(f-1,-1,-1):
    print(i,end='  ')

print('\n')

for n in range(f-1,-1,-1):
    print(n,'==',l[n])

                        ## List Comprehension ## 
list=[] 

for i in range(1,101):
    # print(i,end=',')
    list.append(i)

print(list)

print('\n\n')
# print(dict)
# print(set)

### List Comprerhention Synterx :
#  variable = [ "expresion" for "expresion" in range(start,condition,increment/decrement)]

b=[s for s in range(1,101)]
print(b)

print('\n\n')

# if cond. use kore filtering kore bre korlam even number.
b=[o for o in range(1,101) if o%2==0]
print(b)

print('\n\n')

s="Sporsho"
a=[f for f in s]  # this is creat a list for using comperhansion
print (a) 

print(max([s for s in arr if s < max(arr)]))


                                    ### List Function ####

                # Delete element from list // Remove,Clear,Pop

                ## Function for Delete Element from list :  
                    # 1.del 2.pop() 3.remove()  4.clear()

               # del:

list=[10,20,30,40,50,60,70,80,90]
print(list)

del list[3] # del kono kichuu return kore nah!
print(list)

               # pop():

print(list.pop(7)) #pop return kore.
print(list)

               #remove():

list=[10,20,30,40,50,60,70,80,90]

list.remove(50)
print(list)


                ## Clear() ##

list=[10,20,30,40,50,60,70,80,90]

list.clear()
print(list) #list puro ta faka kore dibe.


             ## Update element form list ::
        
            ## update / insert() / appand() / extends()

# update :

list=[20,30,40,50,60]
list[4]=37
print(list)


#insert() :  # insert(index, object)

list=[20,30,40,50,60]
list.insert(2, 373) #insert jaikono position e boste pare
print(list)

# appand() : [append(object)]

list=[20,30,40,50,60]  #appand sober last e add hoye jabe [Er vator nested list use hoy]
l=[1,2,3,4,5,6,7]
list.append(370)
list.append(l)
print(list)

#extends() :  [extend(iterable)]

list=[20,30,40,50,60]
l=[1,2,3,4,5,6,7]
list.extend(l)
print(list)

                                ## List Function ## 
        # count()  / max() /min() / sort() / reverse() / index() 

# count() :

list=[10,10,20,30,40,506,60,40,70,40,30,20]

a=list.count(40)
print(a)


# max():  [list e boro num. dhakabe, alphabet surru thake dhakabe]

list=[10,10,20,30,40,506,60,40,70,40,30,20]
q=max(list)
print(q)

l=['Hello','World']  #[max() e alphabet revers e asbe ,z y x w..]
q=max(l)
print(q)

h=['Bikrom','Roy']
o=max(h)
print(o)

# min(): 

list=[20,30,40,6,70,80,40,30,10,40,12,34,]
m=min(list)
print(m)

l=['Bikrom','roy']
i=min(l)
print(i)

#sort():

list=[20,30,40,6,70,80,40,30,10,40,12,34]
list.sort()
print(list)

# reverse():

list=[10,20,30,50,10]

list.reverse()
print(list)

# index():

list=[20,30,40,6,70,80,40,30,10,40,12,34]
e=list.index(30)
print(e)

          ##  How Zip Function Work & How to Iterate Over 2+ Lists at the Same Time  ###

l=[1,2,3,5,6,7,8]      
l1=[3,45,6,66,34,45,5] 

for a,b in zip(l,l1):  # vv impt.
        print(a,b)

print('\n')

l=[1,2,3,5,6,7,8]      
l1=[3,45,6,66,34,45,5] 

t=len(l)

for a in range(t):
        print(l[a],l1[a])

                                #### Convert String to List in Python ####

# split() : string ke venghe list e convert korte help kore.

n=input("Enter a value :")
print (n)

l=n.split()
print(l)

  ## user need multiple input:

l=[]
for a in range(1,4):
        n=input("Enter any value " + str(a) + ':')  # here use str()
        
        # print(n) # only input a number
         
        l.append(n) # show me a list item

print(l)


                            #### Implement stack and queue in list data type ####

# Stack : Stack is a linear data structure,
# Last in first out(LIFO) / First in last out (FILO)

"""
Push -> Insert element
Pop -> Deletion element
peek -> Display the last element
Display -> Display list

"""
List=[]
while True:              # kokhono false hobe nah code cholbei 
    c=int(input('''
           1 push
           2 pop
           3 peek
           4 display
           5 exit
        '''))
    if c==1:
        n=input('Enter a value :')
        List.append(n)
        print(List)
    elif c==2:        # Pop : Sober last er element ke delete kore day.
        if len(List)==0:
            print('Empty stack!!')
        else:
            p=List.pop()
            print(p)
            print(List)

    elif c==3:
        if len(List)==0:
            print('Empty stack!!')
        else:
            print('Last stack value :',List[-1])
    elif c==4:
        print('Display stack :',List)
    elif c==5:
        break  # loop thake berr hoberr jonno break
    else:
        print('Invalid Operation..')



# Queue :Linear data structure
# First in First out (FIFO)

List=[]
while True:              # kokhono false hobe nah code cholbei 
    c=int(input('''
           1 push
           2 pop first element
           3 Front element
           4 Last element
           5 display
           6 exit
        '''))
    if c==1:
        n=input('Enter a value :')
        List.append(n)
        print(List)
    elif c==2:        # Pop : Sober last er element ke delete kore day.
        if len(List)==0:
            print('Empty Queue!!')
        else:
            del List[0] #change
        
            print(List)

    elif c==3:
        if len(List)==0:
            print('Empty Queue!!')
        else:
            print('First Queue value :',List[0])
    elif c==4:
       if len(List)==0:
            print('Empty Queue!!')
       else:
            print('Last Queue value :',List[-1])
    elif c==5:
            print('Display Queue!!',List)
       
    elif c==6:
        break  # loop thake berr hoberr jonno break
    else:
        print('Invalid Operation..!!!')

