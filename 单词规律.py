class Solution:
    """
    给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
    """
    def wordPattern(self, pattern: str, str: str) -> bool:
        strs = str.split(' ')
        l_pattern = len(pattern)
        if l_pattern != len(strs):
            return False
        t1 = set(zip(list(pattern), strs))
        t2 = set(list(pattern))
        t3 = set(strs)
        if len(t1) == len(t2) == len(t3):
            return True
        return False

if __name__ == "__main__":
    a = Solution()
    pattern = "abba"
    string1 = "dog cat cat dog"
    print(a.wordPattern(pattern,string1))