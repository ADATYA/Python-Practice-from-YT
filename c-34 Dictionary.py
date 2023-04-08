                        ## Dictionary ## 
# Unorder data type
# key / value
# {}
# mutable,value change kora jay
# key change kora jay nah but value change kora jay ! 

Dict={ 
     'Name' : 'Python',
     'ID '  : '213',
    'Section' :'PC-G', 
}

print(Dict['Name'])
print(Dict['ID'])
# print(Dict['Section'])

for i in Dict:     ## Iteration.
    print(i)
    print(Dict[i])


                            # Dictionary Function 01 ## 

                        # get() / keys() / values() / item()

# get():
#key er through te value returrn kore day.
 
Dict={ 
     'Name' : 'Python',
     'ID '  : '213',
    'Section' :'PC-G', 
}
n=Dict.get('Name')
print(n)

#keys():

for i in Dict.keys():
    print(i)


#values():

for j in Dict.values():
    print(j)


# item():

for k,l in Dict.items(): ## 2 ta parameter use hoy
    print(k,l)


                                # Dictionary Function 01 ## 
                            # del/Pop()-> ei sudhu keys pop korbe.

D={ 
     'Name' : 'Python',
     'ID'  : '213',
    'Section' :'PC-G', }

del  D['Section']  #del
print(D)

print(D.pop('Name')) #pop
print(D)

#dict():

d=dict(name='Bikrom',age='22')
print(d)

# Update():

D={ 
     'Name' : 'Python',
     'ID'  : '213',
    'Section' :'PC-G', }
D.update({'ID':4561})
print(D)

# clear()

D.clear()
print(D)

# insert():

D={ 
     'Name' : 'Python',
     'ID'  : '213',
    'Section' :'PC-G', }

d['desc']="This is a Python"
print(d)

                                    ## Nested Dictionary ## 

Subject={
    'STA':{'chapter':'1-10','durition':'6 month'},
    'DC':{'chapter':'1-5','durition':'6 month'},
    'NM':{'chapter':'1-7','durition':'6 month'},
    'OOP2':{'chapter':'1-8','durition':'6 month'},
}

print(Subject)

print(Subject['STA']['chapter'])  # nested dict er vatorer element ke access kora jay
print(Subject['DC'])
print(Subject['NM'])
print(Subject['OOP2'])

print('\n\n')

for k,v in Subject.items():
    print(k,v['durition'],v['chapter']) #v holo dict er item ke hold kore rakhche jodi ami kono kichuu jante chai dict er vatorer tahole [] er vator mention kore dibo tahole hobe.

      
    #Update():

Subject['DC']['durition']='10 month'
print(Subject['DC']['durition'])

for k,v in Subject.items():
    print(k,v['durition'],v['chapter']) 