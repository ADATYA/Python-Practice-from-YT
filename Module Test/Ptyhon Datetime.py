import datetime

# curent date and time 2 tai day:

x=datetime.datetime.now()
print(x)

# The date contains year,month year,minute,second,microsecond

x=datetime.datetime(2022,4,8)
print(x)

""" 
%b Month short name-- Nov
%B Month full name -- November"
%m month as a number 01-12  12
%y year sort version 23
%Y year full name 2023
%H Hour (00-23) 17
%I houre (00-12) 07
%p AM/PM  AM
%M Minute (00-59) 37

"""

x=datetime.datetime.now()
m=x.strftime("%m")
print(x)
print(m)