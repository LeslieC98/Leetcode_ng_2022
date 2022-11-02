
"""
先用/分割字符串
利用栈先进后出的特性处理上级目录 ..
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []