from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax, rightmax = 0,0
        ans = 0
        while right > left:
            leftmax = max(leftmax,height[left])
            rightmax = max(rightmax,height[right])
        if height[left] < height[right]:
            ans += leftmax - height[left]
            left += 1
        else:
            ans += rightmax - height[right]
            right -= 1

        return ans

