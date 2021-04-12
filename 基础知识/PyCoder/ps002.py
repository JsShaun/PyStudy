
# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))



# list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
# tinylist = [123, 'runoob']
# print (list) # 输出完整列表
# print (list[0]) # 输出列表第一个元素
# print (list[1:3]) # 从第二个开始输出到第三个元素
# print (list[2:]) # 输出从第三个元素开始的所有元素
# print (tinylist * 2) # 输出两次列表
# print (list + tinylist) # 连接列表



st1 = {'Tom', 'Jerry', 'Pite', 'Tom', 'Jack', 'Rose','Shaun'}
print(st1) # 输出集合，集合重复的元素被自动去掉

st2 = set({'Tom', 'Jerry', 'Pite', 'Tom', 'Jack', 'Rose','Shaun'})
print(st2) # 这里同等于上面


if 'Rose' in st2 :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')


a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b) # a 和 b 的差集
print(a | b) # a 和 b 的并集
print(a & b) # a 和 b 的交集
print(a ^ b) # a 和 b 中不同时存在的元素


dict1 = {}
dict1['one'] = "strFirst"
dict1[2] = "numTwo"
print (dict1['one']) # 输出键为 'one' 的值
print (dict1[2]) # 输出键为 2 的值

dict2 = {'name': 'huaz','code':1, 'key2': 'value2'}
print (dict2) # 输出完整的字典
print (dict2.keys()) # 输出所有键
print (dict2.values()) # 输出所有值