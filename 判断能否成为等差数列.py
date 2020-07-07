class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        if not arr:
            return False
        elif len(arr) == 1:
            return True
        arr1 = sorted(arr)
        d = arr1[1]-arr1[0]
        for i in range(1, len(arr1)):
            if arr1[i]-arr1[i-1] != d:
                return False
        return True