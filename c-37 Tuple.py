                        ## Tuple ## 
#Orderd data type
# () paranthasis
# Imutable , value change kora jat nah
#Tuple comma diye likha hoy.
# one or more then are included in tuple
# tuple e value change korra jay nah are insert kora jay nah, tai tuple list er chaya fast kaj kore

T=(20,30,40,70,50,60)

s=T[3]
print(T)
print(s)

e=len(T)
for i in range(e):
    print(i,'==',T[i]) 

for i in T:
    print(i,end= " ")

                                        # Tuple Function 01 ## 

#                                         # min() / max() / count() / index() / Sum() 
T=(10,20,30,40,50,60,70,60,60,80,90)

e=max(T)
print('The maximum number is :',e)

r=min(T)
print("The minimum numberr is :" ,r)

y=T.count(60) # element number gunbe.
print(y)

u=T.index(70)
print(u)

i=T[5] #index value bosbe
print(i)

z=sum(T,30)
print(z)

# #Tuple iteration(loop) err jonno range function use hobe

t=(10,20,30,40,50,60,70,80,90)

l=len(t)
print(t)
print(l)

for i in range(l):
    print(t[i],'=',i)

for i in t:
    print(i,end=" ")

m = max(t)
print(t)
for j in range(m):
    print(j,end=" ")


m = min(t)
print(t)
for j in range(m):
    print(j,end=" ")
    
print('\n')

i= t.index(20)
print(i)