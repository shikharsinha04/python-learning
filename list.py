# list1 = ["ram" ,"shyam",2,343,2.32]  # list is a collection of mutliple type of datatypes,we can change/edit the list
# print(list1,type(list1))
# #slicing
# print(list1[0:2])
# print(list1[1:3])
# print(list1[0:5:2])
# #negalive slicing
# print(list1[-3:])
# print(list1[::-1])
# print(list1[-4:-1:2])
#
#
#
# # list iteration== mean list ke elenments ko line wise dikhna using loop
# list1 = ["ram" ,"shyam",2,343,2.32]
# for i in list1:
#     print(i)      #using for loop
#
#
# print("  ")
#
#
# for i in range(len(list1)):        #using forr loop with range and len()
#     print(list1[i])
#
#
# # list functions
#
# a = ['iron' ,'cap',"thor",'hulk','thor']
# print(a)
# # to find length
# print(len(a))
# #to count occurence of element
# print(a.count('hulk'))
# #to insert elemnt in default-- end
# a.append('hulk')
# print(a)
# #to aad at position index
# a.insert(1,'spidy')
# print(a)
#
# # to remove by using value
# a.remove('hulk')
# print(a)
#
# #th remove using index
# a.pop()
# print(a)
# a.pop(2)
# print(a)

a1 = ['iron' ,'cap',"thor",'hulk','thor']
b1 = []
print(a1)
print(b1)
b1 = a1.copy()      #copy list
print(b1)

print(a1.index("iron"))       #for accesing

c1 = [1,2,5]
a1.extend(c1)      #for extending the list
print(a1)


print(a1.reverse())
print(a1)            #for reversing


c1.sort()
print(c1)
d1 = ["Aregentina ","america","india"]     #for sorting
d1.sort()
print(d1)

d1.clear()
print(d1)       #for clearing


