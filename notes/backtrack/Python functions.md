```python
## 字母大小写问题
- string.upper() #转化string中所有字母大写
- string.lower() #转化string中所有字母小写
- string[0].lower() ##如果要只转化一个字母的大/小写利用slicing


## 排序:
- list.sort():
在list原来的基础上sort不额外增加空间即 space complexity为o(1)\
list.sort() 只能用于list\
sort() 有两个变量 一个是key,另外一个是reverse = False(默认)\
list.sort(key = lambda x:x[0], reverse = True) ##这里lambda x:x[0] 为对每一个元素的[0]作为排序的标准

- sorted():
用额外的空间 即space complexity 为o(n)\
对于任何的iterable都可以不只是 list\
sorted() 有三个变量 要进行排序的iterable,key,reverse\
sored(iterable, key,reverse)  #reverse == True即从大到小排序, fasle即从小到大排序

- quesiton: 如果多个标准的sort? eg:先根据a sort,再根据b sort\
intervals = [[1,100],[11,22],[1,11],[2,12]]\
intervals.sort(key=lambda x:(x[0],x[1]))\

print(intervals) # [[1, 11], [1, 100], [2, 12], [11, 22]]


- examples:
#对list1的index1元素进行降序排序
list1 = [("a",1),("b",2),("c",3)]\
list1.sort(key = lambda x:x[1], reverse = True) ##[('c', 3), ('b', 2), ('a', 1)]\
list2 = sorted(list1,key = lambda x:x[1], reverse=True) ##[('c', 3), ('b', 2), ('a', 1)]

## map()映射:
- 定义&语法:
map(function, iteration)
fun: 每一个iteration的元素都经过这个fun的映射
iteration: 一个可遍历的object
return: 输出为一个list

- examples:
numbers1 = [1,2,3]\
numbers2 = [4,5,6]\
result = map(lambda x,y:x+y, numbers1,numbers2)\
print(list(result)) #[5,7,9]

- leetcode的时候遇到的(把每一个string转换为int)
string1 = "123"\
result = map(int,string1)\
print(result) #[1,2,3]

## 把string分割开相同的部分:
- example:
import textwrap
word1 = "ab"
textwrap.wrap(word1, 1) ##  ['a', 'b'] 分割等价的长度为1的string

## iterative object slicing:
- List[Initial:End:IndexJump]:\
Lst = [50, 70, 30, 20, 90, 10, 50]\
Lst[:] ## [50, 70, 30, 20, 90, 10, 50]

- negative indexes:\
[50, 70, 30, 20, 90, 10, 50]\
-7,  -6, -5, -4, -3, -2, -1

- reversed list using negative integer as IndexJump:\
Lst[::-1] ## [50, 10, 90, 20, 30, 70, 50]\
bucket = [1,7,6,7]\
bucket[-2:] ## 从-2开始一直到最后 [6,7]


--* functools.cache
usage:
import functools
@functools.cache

returning remembered result rather than computing the result again
purpose: optimzie time and space complexcity“
```

