# fibonacci

# a= 0
# b=1
# num = int(input("eneter no. "))
# for i in range(2,num):
#     print(a)
#     c=a+b
#     a=b
#     b=c

# prime or not
# num = int(input("Enter a number: "))
# if num <= 1:
#     print(" not prime")
# else:
#     for i in range(2,num):
#        if num%i == 0:
#           print(" not prime")
#           break
#     else :
#           print(" prime")



# palindrone or not
while True:
    num = int(input("Enter a number: "))
    rnum = int(str(num)[::-1])

    if rnum == num:
        print("Palindrone")
    else:
        print("Not ")
    y = input("continue yes /no")
    if y == "yes"or y == "YES":
        break
