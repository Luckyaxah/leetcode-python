class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        for char in t:
            if char in d:
                d[char]-= 1
            else:
                return False
        for i in d:
            if d[i] != 0:
                return False
        return True

if __name__ == "__main__":
    a = Solution()
    print(a.isAnagram('anagram','nagaram'))
    print(a.isAnagram('rat','cat'))