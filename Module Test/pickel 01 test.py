# import pickle

# l=[10,20,30,40,50]

# file=open("pickel02test.txt",'wb')

# pickle.dump(l,file)
# file.close()

import pickle 
file=open("pickel02test.txt",'rb')

l=pickle.load(file)
print(l)