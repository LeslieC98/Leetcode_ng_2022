## 1
from typing import List
"""
(a&b) + (a|b)
(a^b) + (a&b)*2
(^a&b) + (a&^b) + 2*(a&b)
class Solution:
##2
n-1

"""



##3
class Solution:
    def boring_array(self, a: str, b: str):

        if len(a) != len(b):
            return False
        arr1, arr2 = a.split(), b.split()
        if len(a) != len(b):
            return False
        nums1, nums2 = [], []
        for i in range(len(arr1)):
            nums1.append(int(arr1[i]))
            nums2.append(int(arr2[i]))
        nums1.sort()
        nums2.sort()

        for i in range(len(nums1)):
            if nums1[i] != nums2[i] and nums1[i] + 1 != nums2[i]:
                print(nums1)
                print(nums2)
                return False

        return True

##4
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [amount + 1] * (amount + 1)  # 初始化为一个较大的值，如 +inf 或 amount+1
        dp[0] = 0  # 合法的初始化

        # 完全背包：优化后的状态转移
        for i in range(1, n + 1):  # 第一层循环：遍历硬币
            dp2 = [amount + 1] * (amount + 1)  # 滚动数组
            for j in range(amount + 1):  # 第二层循环：遍历背包
                if j < coins[i - 1]:  # 容量有限，无法选择第i种硬币
                    dp2[j] = dp[j]
                else:  # 可选择第i种硬币
                    dp2[j] = min(dp[j], dp2[j - coins[i - 1]] + 1)
            dp = dp2

        ans = dp[amount]
        return ans if ans != amount + 1 else -1


class Solution:
    def coinChange(self, sizes: List[int], requirement: int) -> int:

        dp = [requirement + 1] * (requirement + 1)  # 初始化为一个较大的值，如 +inf 或 amount+1
        dp[0] = 0  # 合法的初始化；其他 dp[j]均不合法

        # 完全背包：优化后的状态转移
        for size in sizes:  # 第一层循环：遍历硬币
            for j in range(size, requirement + 1):  # 第二层循环：遍历背包【正序】
                dp[j] = min(dp[j], dp[j - size] + 1)  # 可选择当前硬币

        ans = dp[requirement]
        return ans if ans != requirement + 1 else -1

##5
class Solution:
    def ways(self, forest: List[List], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(forest), len(forest[0])
        # dp[m][n][k]
        dp = [[[0] * k for j in range(n)] for i in range(m)]

        # nums[i][j]: how many apples in forest[i:][j:]
        nums = [[False] * n for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n - 1, -1, -1):
                has_poplar = forest[i][j] == 2
                if i == m - 1 and j == n - 1:
                    nums[i][j] = has_poplar
                elif i == m - 1:
                    nums[i][j] = has_poplar + nums[i][j + 1]
                elif j == n - 1:
                    nums[i][j] = has_poplar + nums[i + 1][j]
                else:
                    nums[i][j] = has_poplar + nums[i + 1][j] + nums[i][j + 1] - nums[i + 1][j + 1]

        # dp[i][j][p] = sum(dp[x][j][p] for x in [i+1,m-1]) + sum(dp[i][y][p] for y in [j+1, n-1])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if nums[i][j]:
                    dp[i][j][0] = 1
                for p in range(1, k):
                    for x in range(i+1, m):
                        if nums[i][j] - nums[x][j]:
                            dp[i][j][p] += dp[x][j][p-1] % mod
                    for y in range(j+1, n):
                        if nums[i][j] - nums[i][y]:
                            dp[i][j][p] += dp[i][y][p-1] % mod
        return dp[0][0][k-1] % mod



