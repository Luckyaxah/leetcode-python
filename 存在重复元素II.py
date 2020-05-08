class Solution:
    """
    给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，
    使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
    """
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        d ={}
        for ind,val in enumerate(nums):
            if d.get(val):
                for index in d.get(val):
                    if abs(index-ind) <= k:
                        return True
                d.get(val).append(ind)
            else:
                d[val] =[ind]
        return False

if __name__ == "__main__":
    a = Solution()
    print(a.containsNearbyDuplicate([1,2,3,1],3))
    print(a.containsNearbyDuplicate([1,0,1,1],1))
    print(a.containsNearbyDuplicate([1,2,3,1,2,3],2))
    