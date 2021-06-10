class Solution:
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes for x in range(L, R+1))

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation/solution/er-jin-zhi-biao-shi-zhong-zhi-shu-ge-ji-suan-zhi-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
