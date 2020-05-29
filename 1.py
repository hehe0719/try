# # # # 求1至10的和
# # # sum = 0
# # # for i in range(1,11):
# # #     print(i,end = ' ')
# # #     sum = sum + i
# # # print("-----")
# # # print(sum)
# #
# # a = 'hello'
# # b = 'world'
# # print(len(a))
# # print(a + b)
# # #字符串从0开始计数，取片取不到最后一位，即开区间
# # print(a[1:4])
# # print(a[4:])
# # print(a[0:4])
# # # 字符串反取，同样开区间
# # print(a[4:1:-1])
# # # 统计字符串中某字符出现的次数
# # print(a.count('l'))
#
# c = [1,2,3,4,5,6,9,9,9,10]
# # for i in c:
# #     print(i)
# print(len(c))
# print(c.count(9))
# # append只能加1个数
# c.append(11)
# print(c)
# c.sort()

# d = {'one':'this is one','two':'this is tow'}
# print(d['one'])
# print(d)
# 返回是列表
# print(d.keys())
# print(d.values())
# for value in d.values():
#     print(value)
# 打印字典具体某个键对应的值
# print(d.get('one'))
# 为字典增加元素
# d['three'] = 'this is three'
# 删除字典某个元素
# d.pop('one')
# print(d)
# #删除字典d
# d.clear()

# sum = 0
# i= range(11)
# for m in i:
# #求[0,11)的和
#     sum += m
# print(sum)

a = [2,3,1,4,3,8,4,10]
a.sort()
print(a)
# 逆序排列
a.sort(reverse=-1)
print(a)


