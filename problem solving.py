# program to display person name , age , address in three diff lines
name = "shikhar"
age = 22
address =  "python bazar"


print( "Your name is", name,"\nage is", age ,"\naddress is", address )

# program to swap two variables
a = 22
b = 23

print(a,b)

temp = a
a= b
b = temp
print(a,b)

# program to convert float to int

a1 = 12.2
print("before",type(a1))

a1 = int(a1)
print("after",type(a1))

# to take info from user

stu_name = input("Enter your name:")
stu_age = int(input("Enter your age:"))
stu_address = input("Enter your address:")

print('\n',stu_name,"\n",stu_age,"\n",stu_address)

# take int input from user and convert to float
stu_age = float(stu_age)
print(stu_age)
