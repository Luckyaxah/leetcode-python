class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s)-1
        while head < tail:
            temp = s[head]
            s[head] = s[tail]
            s[tail] = temp
            head += 1
            tail -= 1
        # print(s)

if __name__ == "__main__":
    a =  Solution()
    print(a.reverseString(["h","e","l","l","o"]))
