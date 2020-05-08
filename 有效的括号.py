class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        for char in s:
            if char in ['(','{','[']:
                p.append(char)
            if char == ')':
                if not p or p.pop() != '(':
                    return False
            elif char == '}':
                if not p or p.pop() != '{':
                    return False
            elif char ==  ']':
                if not p or p.pop() != '[':
                    return False
        if not p:
            return True
        return False



if __name__ == "__main__":
    a = Solution()
    print(a.isValid("()"))