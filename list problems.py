# program to swap 1st and 4th elemet

l1 = [2,3,54,18]
temp = l1[0]
l1[0] = l1[3]
l1[3] = temp

print(l1)
#to insert new element ant 2nd position
l1.insert(1,'new')
print(l1)
#to remeove 3rd position elemet
l1.pop(2)
print(l1)

#to multiply all teh elemnet of list
l2 = [2,4,6]

print(l2[0]*l2[1]*l2[2])


mul = 1
for i in l2:
    mul *= i
print(mul)

#for finding largest and smallest no.
l3 = [20,40,6]
l3.sort()
print(l3)
print("shortest no. is ", l3[0])
print("longest no. is ", l3[-1])
