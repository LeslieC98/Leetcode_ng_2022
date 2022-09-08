# 1. 题目关键字

- is the array sorted?
- time complexity requries o(logn)

## 1.1 什么时候可用？

给定的**Array**是**排序好**的数组，或者题目需要时间复杂度为**O(logN)**

要注意，【**单调性】**不是二分查找的必要条件，只要数组中的元素排列满足某种特定的【**次序关系**】，就可以使用二分查找。在后面我们会看到一些具体例子。

Binary search 是**分治思想（Divide and conquer）**的体现



# 2. 例题

## 35. Search Insert Position



Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

 

**Constraints:**

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-104 <= target <= 104`

总共有n个元素，每次查找的区间大小就是n，n/2，n/4，…，n/2^k（接下来操作元素的剩余个数），其中k就是循环的次数。
由于n/2^k取整后>=1，即令n/2^k=1，
可得k=log2n,（是以2为底，n的对数），所以时间复杂度可以表示O()=O(logn)

```python
##time: o(logn)这里是输入数组的长度
##space: o(1)

##q: why binary search is logn?
##a: each time binary search is gonna divided by 2, but how many times that binary search need to do so?
##a_: log 2^(n) = x -> x times


##左闭右闭，可以取到
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1 ##索引从0开始所以需要len(nums) - 1
        while l <= r:
            mid = l+(r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                r = mid -1
        return l  ##while 循环里只把区间分成两个部分，退出循环的时候一定有 left == right 成立，因此返回 left 或者 right 都可以。
```

