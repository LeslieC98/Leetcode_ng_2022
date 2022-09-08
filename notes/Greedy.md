# 1. 什么是贪心

**贪心的本质是选择每一阶段的局部最优，从而达到全局最优**。



# 2. 什么时候使用？

**贪心没有套路，说白了就是常识性推导加上举反例**



# 3. 步骤

贪心算法一般分为如下四步：

- 将问题分解为若干个子问题
- 找出适合的贪心策略
- 求解每一个子问题的最优解
- 将局部最优解堆叠成全局最优解



# 4. 例题

### 455. Assign Cookies

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

**Example 1:**

```
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
```

**Example 2:**

```
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
```

 

**Constraints:**

- `1 <= g.length <= 3 * 104`
- `0 <= s.length <= 3 * 104`
- `1 <= g[i], s[j] <= 231 - 1`

#### **Ans**: 先排序，倒序最好。让最大饼干的满足最贪心的小朋友，如果当前的饼干不能满足当前的小朋友，就找下一个小朋友看是否能满足

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        
        child,cookie,res = 0,0,0
        ##先排序，倒序最好。让最大饼干的满足最贪心的小朋友，如果当前的饼干不能满足当前的小朋友，就找下一个小朋友看是否能满足
       


        while cookie <len(s) and child <len(g):
            if s[cookie] >= g[child]: # checking if cookies are more or equal to a child greedy.
                child += 1 ## if child greedy is getting fulfilled it will be content, and will increase out counter.
                cookie += 1
                res +=  1
                
            else:
                child+= 1 
        
        return  res
    """
    
    child[2,1]
    cookie [3,2,1]
    round 1
    s[0] = 3, g[0] = 2 s[0] >= g[0]
    child = 1, cookie = 1 s[1] = 2, g[1] = 1, res = 1##成功让最大饼干满足最贪心的小朋友
    
    round 2 
    s[1] = 2, g[1] = 1 s[1] >= g[1]
    child = 2, cookie = 2  child <len(g)不满足条件，return res
    “”“
```

# 5. 调度问题Interval Scheduling

**看到[start, end]类型的数组可以考虑贪心**

