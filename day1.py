
#print,take input,show output;

print("Hello, World!")
str = "This is a sample string."
print(str)
st= input("Enter something: ")
print("You entered:", st)


# Variables plus minus
n1 = 42
n2 = 3.14
n3 = n1+n2
n4 = n1-n2
n5 = n1*n2
n6 = n1/n2
print("The sum of", n1, "and", n2, "is", n3)
print("The difference of", n1, "and", n2, "is", n4)
print("The product of", n1, "and", n2, "is", n5)
print("The quotient of", n1, "and", n2, "is", n6)


print("This is the end of the program.")

# name age print 
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello", name, "you are", age, "years old.")  

# calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))    
print("your numbers are ", num1, "and", num2)
sign = input("Enter an operator (+, -, *, /): ")
print("You selected operator:", sign)
if sign == '+':
    result = num1 + num2
    print("The sum is:", result)
elif sign == '-':
    result = num1 - num2
    print("The difference is:", result)
elif sign == '*':
    result = num1 * num2
    print("The product is:", result)
elif sign == '/':
    if num2 != 0:
        result = num1 / num2
        print("The quotient is:", result)
    else:
        print("Error: Division by zero is not allowed.")


#marks average
maths = float(input("Enter your maths marks: "))        
english = float(input("Enter your english marks: "))
science = float(input("Enter your science marks: "))
print("Your marks are ", maths, "in maths", english, "in english and", science, "in science")
total = maths + english + science
average = total / 3     
print("Your total marks are:", total)
print("Your average marks are:", average)