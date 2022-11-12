class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = ''
        for i in s:
            if ord('A') <= ord(i) <= ord('Z'):
                ans+=(chr(ord(i) + 32))
            elif ord('a') <= ord(i) <= ord('z'):
                ans+=(chr(ord(i) - 32))
        return ans

if __name__ == '__main__':
    s = "BoyuZhang"
    print(Solution().toLowerCase(s))