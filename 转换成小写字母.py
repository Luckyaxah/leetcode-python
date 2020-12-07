class Solution:
    def toLowerCase(self, str1: str) -> str:
        s = ''
        for c in str1:
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                s += chr(ord('a') + ord(c) -  ord('A'))
            else:
                s += c
        return s