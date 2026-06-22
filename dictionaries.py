stu_dic = {
    "name":"john","age":22,"city":"New York"
}
print(stu_dic)
print(stu_dic["name"])
print(stu_dic.keys())
print(stu_dic.values())


#iteration

for i in stu_dic.items():
    print(i)
for i in stu_dic.values():
    print(i)
for i in stu_dic.keys():
    print(i)


#nested dictionary

stu2_dic = {1:{"name":"john","age":22,"city":"New York"},2:{"name":"jon","age":12,"city":"New"}}
print(stu2_dic)
print(stu2_dic.keys())
print(stu2_dic.values())
print(stu2_dic[2]["age"])

for i in stu2_dic.items():
    print(i)

























