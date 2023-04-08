                        ## Set ## 

# Unorder /Unindex
#{}
# Desinding order e value print kore [random ans ase]

# s={10,30,40,50,50,70}
# print(s)

# for i in s:
#     print(i)

#                         ## Set Function 

                        ## set()/ add()/ pop() /remove()/cleare()/dicard()/update()

 # List ke Set e convert [v.v.impt]

l=[10,20,30,40,50]

s=set(l)
print(s)

s={20,45,56,67,70}
p=s.pop()
print(p)

print()

print(s)

print()

s={20,45,56,67,70,80,90}

s.remove(67)    #remove
print(s)


print()
 
s.discard(56)  #dicard
print(s)

s.clear()  #clear

print(type(s.clear()))

print(s)

s={20,45,56,67,70,80,90}

l=[23,24,27,37]

s.update(l)  #update
print(s)