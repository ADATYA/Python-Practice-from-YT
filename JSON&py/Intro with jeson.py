""" JSON (JavaScript Object Notation)
    It is strongly used for storing a transfering data between the browser and the server 
    JSON is text support JSON with build in package called json"""

## What is API: API is mainly used in two devise as a postman, API is working as a third party to transfer a same data one to another side.
## it is use in app to server connection.
## API formet is create in JSON.

'''
JSON support mainly 6 data type ::
1.string
2.number
3.boolian
4.null
5.object
6.array

In python JSON as a string for example:

p='{"name":"CSE","dept":["cse","low","bba"]}'

'''

# How to create a JSON object :

import json

d={
    'course_name':'Python',
    'fees': 2000
}

f=json.dumps(d)

print(type(f))
print(f)
