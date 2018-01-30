#coding:utf-8

# 这是一个词频统计的例子

# path = 'Walden.txt'
# with open(path,'r') as text:
#     words = text.read().split()
#     print(words)
#     for word in words:
#         print('{}-{} times'.format(word,words.count(word)))

# 结果有一些奇怪：
# 1. 有一些带标点符号的单词被单独统计了次数；
# 2. 有些单词不止一次地展示了出现的次数；
# 3. 由于 Python 对大小写敏感，开头大写的单词被单独统计了。


import string
import time

t0 = time.clock()
path = 'Walden.txt'

with open(path,'r') as text:
    # string.punctuation包含所有标点符号
    # 在文字的首位去掉了连在一起的标点符号，并把首字母大写的单词转化成小写
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    # 将列表用 set 函数转换成集合，自动去除掉了其中所有重复的元素
    words_index = set(words)
    # 创建了一个以单词为键（key）出现频率为值（value）的字典
    counts_dict = {index:words.count(index) for index in words_index}

# 打印整理后的函数，其中lambda 表达式 key=lambda x: counts_dict[x] ，可以暂且理解为以字典中的值为排序的参数
for word in sorted(counts_dict,key=lambda x: counts_dict[x], reverse=True):
    print('{} -- {} times'.format(word, counts_dict[word]))

print time.clock() - t0, "seconds process time"