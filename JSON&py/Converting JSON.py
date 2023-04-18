#If you have a json string you can parse it by using the json .loads() method.

# import json

#some JSON:
# x='{"cname":"python","fees":3720,"duration":"2 months"}'

#parrse x:
# y=json.loads(x)

#the result is Python dictionary:

import json

d ='{"cname":"python","fees":3720,"duration":"2 months"}'

x = json.loads(d)

print(type(x))
print(x)

for a in x:
    print(a,x[a])