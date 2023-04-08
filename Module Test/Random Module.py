                                ## Random Module ##
   
import random

# randint():
n=random.randint(2,8)
print(n)

# randrange(): 

# # ei kono last paramiter err value dhakabe nah ,ex:4
n=random.randrange(2,4)
print(n)

#choice():

l=[10,20,30,40]
l1=random.choice(l)
print(l1)

 # rando()akti module / function
 # shuffle()
 # uniform()

r= random.random()  # float value dhakay
print(r)

l=[10,20,30,40]
random.shuffle(l)
print(l)

u=random.uniform(3, 9)
print(u)