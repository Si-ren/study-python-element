# loop
str1 = 'sirius wang'
for i in str1:
    if i == 'a':
        continue
        # break
    # print(i)
else:
    print("finish for")

# strings
str1 = "0123456789"
# str1 = input("Input your name:")
print(type(str1))
print("我的名字是%s." % str1)
print(f'my name is {str1}')
print(f'String index: {str1[-1]}')
# [开始位置：结束位置：步长]
print(f'String slip step 2: {str1[0:-1:2]}')
# 负数为倒序
# 正数为正序
print(f'String slip step 2: {str1[-1:-4:-1]}')
# find()  return -1 or str index
# index() count()  方法类似
print(str1.find("456",1,8))

list1 = ["Tom","Jerry","Jack"]
print("Tom" in list1)
print("Tom1" not in list1)
list1.extend(['Siri','Merry'])
list1.append('Append')
list1.insert(1,"Bruce")
# pop()移除最后一个
# del list[0] 删除指定
# remove() 移出第一个匹配项
name_list=list1.pop()
print(name_list)

# sort()排序,默认升序，reverse=True降序
num_list=[2,3,1,4,6,5]
# 逆置，不排序
num_list.reverse()
print(num_list)
list1.sort(reverse=True)
print(list1)

# copy()复制
