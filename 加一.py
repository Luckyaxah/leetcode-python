class Solution:
    def plusOne(self, digits):
        len_digits = len(digits)
        ind = len_digits - 1

        while True:
            if digits[ind] + 1 == 10:
                digits[ind] = 0
                ind -= 1
            elif ind == -1:
                digits.insert(0,1)
                break
            else:
                digits[ind] += 1
                break
        return digits
        


if __name__ == "__main__":
    a = Solution()
    print(a.plusOne([9,9,9]))