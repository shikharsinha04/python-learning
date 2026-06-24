# modules is a type of function that we can use that by importing/calling this
from sys import modules

import addmodule
#in built modules--datetime,math , random.

# import datetime
# x= datetime.datetime.now()
# print(x)
# x=datetime.datetime.time(datetime.datetime.now())
# print(x)
# x= datetime.datetime.date(datetime.datetime.now())
# print(x)
# x= datetime.datetime.today()
# print(x.day)






# import math
# a = math.pi
# print(a)
# b = math.pow(4, 2)
# print(b)
# c = max(78, 8)
# print(c)
# d = min(7, 8)
# print(d)
# e = math.sqrt(49)
# print(e)





# import random
# a = random.randint(1,6)
# print("your dice no. is :",a)
# b = ("head","tail")
# b1 = random.choice(b)
# print("coin position : ",b1)


#using self built module
import addmodule as amc
a= addmodule.add(23,34)
print(a)









