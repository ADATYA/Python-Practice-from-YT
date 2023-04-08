# how to module work (way-1st)

import Module1 as m  # use the alias [as] to small the module name

print(m.sum(10,20))
print()
print(m.mdl(20, 30))



# how to module work (way-2nd)

from Module1 import sum 

print(sum(10,20))  # eikhane . module use kora lagche nah 


from Module1 import *  # *eita use korar fole sob guloke aksathe dhaka jay

print(sum(10,20))
print(mdl(10,20))