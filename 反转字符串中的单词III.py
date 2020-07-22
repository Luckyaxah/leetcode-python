class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for i in range(len(l)):
            l[i] = l[i][::-1]
        return ' '.join(l)

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(Solution().reverseWords(s))