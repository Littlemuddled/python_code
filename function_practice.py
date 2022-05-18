# # while循环实现
# i = 0
# while i < 9:
#     i += 1
#     j = 0
#     while j < i:
#         j += 1
#         print(i, '*', j, '=', i * j, end='\t', sep='')
#     print()
#
# # for循环实现
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(i, '*', j, '=', i * j, end='\t', sep='')
#     print()


# 一匹大马能驮3担货，一批中马能驮2担，两匹小马驮一担货，如果一百匹马驮一百担货，大中小马各需要多少匹
# 解：假设大马有 x 匹，中马 y  小马：100-x-y
# for x in range(0, 100 // 3 + 1):
#     for y in range(0, 100 // 2 + 1):
#         if 3 * x + 2 * y + (100 - x - y) * 0.5 == 100:
#             print(x, y, (100 - x - y))

# 一张纸厚度大约0.08mm，队折多少次后能达到珠穆朗玛峰的高度(8848.13m)
# height = 0.08 / 1000
# count = 0
# while True:
#     height *= 2
#     count += 1
#     if height >= 8848.13:
#         break
# print(count)

# str = 'abcdefg'
# print(str.find('a'))
#
# list1 = ['a', 'b', 'c', 'd']
# print(list1.index('a'))
# print(id(str))

# 1.编写函数求 1+2+3+……+n的和
def num(n):
    m = 0
    for i in range(1, n + 1):
        m += i
    return m


# 2.编写函数求多个无数中的最大数
def max_number(*args):
    x = args[0]
    for arg in args:
        if arg > x:
            x = arg
    return x


# 3.编写一个函数，实现摇骰子的功能，打印n个骰子的点数和
import random


def get_num(n):
    m = 0
    for i in range(n):
        x = random.randint(1, 6)
        m += x
    return m


# 4.编写一个函数交换指定字典的key和value (字典表达式)
# 方法一
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {}
for k, v in dict1.items():  # 把dict1里面的k,v拿出来放到dict2里面
    dict2[v] = k
dict1 = dict2
print(dict1)
# 方法二
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict1 = {v: k for k, v in dict1.items()}
print(dict1)


# 5. 编写一个函数，提取指定字符串中所有字母，然后拼接在一起产生一个新的字符串
def get_str(word):
    new_str = ''
    for w in word:
        if w.isalpha():
            new_str += w
    return new_str


# 6.写一个函数，求多个数的平均值
def average_value(*args):
    num = 0
    count = 0
    for i in args:
        num += i
        count += 1
    average = num / count
    return average


# 7.写一个函数默认求10的阶乘，也可以求娶她数字的阶乘
def get_factorial(n=10):  # n=10默认为10
    m = 1
    for i in range(1, n + 1):
        m *= i
    return m


# 8.写一个自己的capitalize函数，能够将指定字符串首字母变成大写
def my_capitalize(word):
    c = word[0]
    if 'a' <= c <= 'z':
        new_str = word[1:]
        return c.upper() + new_str
    return word


# 9.写一个自己的endswith函数，判断一个字符串是否以指定字符串结束
def my_endswith(old_str, new_str):
    return old_str[-len(new_str):] == new_str


# 10.写一个自己的isdigit函数，判断一个字符串是否是纯数字字符串
def my_isdigit(old_str):
    for s in old_str:
        if not '0' <= s <= '9':
            return False
    return True


# 11.写一个自己的upper函数，将一个字符串中所有的小写变成大写
def my_upper(m_str):
    new_str = ''
    for s in m_str:
        if 'a' <= s <= 'z':
            upper_s = chr(ord(s) - 32)
            new_str += upper_s
        else:
            new_str += s
    return new_str


# 12.写一个自己的rjust函数，创建一个字符串的长度是指定长度，原字符串在新字符串中右对齐，剩下的用指定的字符填充
def my_rjust(old_srt1, a, c):  # a是指定新字符串的长读，c是填充的字符
    new_str = ''
    n = len(old_srt1)  # 原字符串的长度
    for i in range(a - n):
        new_str += c
    new_str += old_srt1

    return new_str


# 13.写一个自己的index函数，统计指定列表中指定元素的所有下标，如果列表中没有指定元素返回-1.
def my_index(list1, a):  # a为指定元素
    count = 0
    sub = []
    for i in list1:
        count += 1
        if i == a:
            sub.append((count - 1))
    if not sub:
        return -1
    else:
        return sub


# 14.写一个自己的len函数统计指定序列中元素的个数
def my_len(*args):
    count = 0
    for i in args:
        count += 1
    return count


# 15.写一个函数实现自己的in操作，判断指定序列中指定的元素是否存在
def my_in_1(it, ele):  # e表示指定元素
    for i in it:
        return i == ele
    #     if i == ele:
    #         return True
    # else:
    #     return False


def my_in_2(it, ele):
    for i in it:  # 遍历拿到的的是key
        return it[i] == ele
    # for k, v in it.items():
    #     return v == ele


# 写一个自己的replace函数，将指定字符串中指定的旧字符串转换成指定的新字符串
def my_replace(all_str, old, new):
    # return new.join(old_str.split(old))  # 一种方法
    new_str = ''
    i = 0
    while i < len(all_str):
        temp = all_str[i:i + len(old)]  # 将字符串切片，挨个查看
        if temp != old:
            new_str += all_str[i]
            i += 1  # 每次只检查一个字符
        else:
            new_str += new
            if len(new) > len(old):
                i += len(old)
            else:
                i += len(new)
    return new_str


# 写一个自己的max函数，获取指定序列中元素的最大值。如果序列是字典，取字典的最大值
def my_max(seq):
    if type(seq) == dict:  # 判断是否是字典
        seq = list(seq.values())
    x = seq[0]
    for i in seq:
        if i > x:
            x = i
    return x


print(num(10))
print(max_number(6, 5, 4, 8, 9))
print(get_num(4))
print(get_str('sf4s15fv4b55m'))
print(average_value(1, 2, 3, 4, 5, 6))
print(get_factorial(5))
print(my_capitalize('hello'))
print(my_endswith('hello', 'llo'))
print(my_isdigit('123456'))
print(my_upper('Hello'))
print(my_rjust('abc', 8, '#'))
print(my_index([1, 2, 3, 4, 5, 3], 8))
print(my_len('a', 'b', 'c', 'd'))

print(my_in_1(['a', 'b', 'c', 'd'], 'r'))
print(my_in_2({'name': 'lisa', 'age': 25, 'height': 170}, 'lisa'))

print(my_replace('fuck you,fuck you.', 'fuck', 'love'))
print(my_max([1, 2, 3, 8, 4, -5, -1, 5, 6]))
print(my_max((-1, -8, -9, -1, -5)))
print(my_max({'小明': 55, '张三': 69, '小红': 98}))
