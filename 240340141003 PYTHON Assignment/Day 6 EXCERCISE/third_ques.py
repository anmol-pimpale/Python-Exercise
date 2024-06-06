# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)

class My_exception(Exception):
    pass

try:
    age=int(input("enter the age:"))
    
    live=age*365
    
    if live > 101:
        raise My_exception
    else:
        print(f"you live for {live} days")
except My_exception:
    print(f"you live for {live} days you will die soon")
    