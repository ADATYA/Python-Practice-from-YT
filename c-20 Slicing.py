I="Bikrom Roy"

print(I[0:6:1])
print(I[0::1])
print(I[-1::-3])
print(I[-1::-1]) #revers


B="Aditya Roy"
#print(len(B))
W=len(B)
print(W)

for a in range(W):
    print(B[a])

print("\n\n")

for i in range(W-1,-1,-1): #Reverse
    print(B[i] ) 


                        ## String function 1 ###
    
                    ## lower,upper,title,capitalize.

s="Bikrom adatya roy"
n=s.lower()
print(n)

d=s.upper()
print(d)

c=s.title()
print(c)

q=s.capitalize()
print(q)

                        ### String function  2 ###

                    # find,index,isalpha,isdigit,isalnum.

b="Welcome"
t=b.find('l') #[Find show the index number] [Find er modha kono word nah thakle -1 dhakhabe]
t=(b.find('l',2))
print(t)

p=b.index('o')
print(p)


#isalpha() represent all the alphabet then it return True otherwise it print False. 

b="Bikrom"
c=b.isalpha() #[True]
print(c)

b="Bikrom 12345"
c=b.isalpha()   #[False]
print(c)

#isdigit() represent all the 
s="1234"
b=s.isdigit()  #[True]
print(b)

s="1234 Bikrom"
b=s.isdigit()  #[False]
print(b)


#isalnum [String/ digit jai thakuk nah kano ans diye dibe]

d='bikromroy1234'
print(d.isalnum())

d='1234'
print(d.isalnum())

d='bikromroy'
print(d.isalnum())

# Spacial charecter string err majhe dile False asbe. 

d='bikrom # roy1234'
print(d.isalnum())

d='bikrom ! roy1234'
print(d.isalnum())

d='bikrom @ roy1234'
print(d.isalnum())

d='bikrom % roy1234'
print(d.isalnum())

d='bikrom * roy1234'
print(d.isalnum())

d='bikrom & roy1234'
print(d.isalnum())


                            ### String function  3 ###

                            ## Python chr() and ord()

# It is converting integer value 37 to ASCII charecter('A')

# Ascii "A" start hoy "65" thake.

a=65
print(type(a))  # ---> intiger

print(type(chr(a))) #--->> String

# ord() work as convert Ascii unicode char to int.

d="S"
print(type(ord(d))) # ---> intiger

d="N"
print(ord(d))

d="B"
print(ord(d))

d="A"
print(ord(d))

# d="Sporsho"
# print(ord(d))  #TypeError: ord() expected a character, but string of length 7 found.and

                            ### String function  4 ###
                            ## Formet() method ##

""" A= "Welcome to {fname}{lname}".formet(fname='Bikrom',lname='Roy')
    B= "Welcome to {0}{1}".formet('Bikrom','Roy')" 
    C= "Welcome to {}{}".formet("Bikrom','Roy') """

B= "Welcome {} to {} DIU".format('hello','37')
print(B)

B="Hi this {0} Bikrom {1}".format('is',"Roy")
print(B)

B="Welcome to {a} {s}".format(a="Roy",s="Villa")
print(B)

B="Welcome to {a:30} {s}".format(a="Roy",s="Villa")
print(B)   

B="Welcome to {a:^30} {s}".format(a="Roy",s="Villa")
print(B)    # ^ ----10----


B="Welcome to {a:>30} {s}".format(a="Roy",s="Villa")
print(B)   # > ---------10

B="Welcome to {a:<30} {s}".format(a="Roy",s="Villa")
print(B)   # < 10---------

