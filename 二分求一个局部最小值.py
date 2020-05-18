def getLocalMin(nums):
    if len(nums)<2:
        return 0
    start = 0
    end = len(nums)-1
    if nums[start]<nums[start+1]:
        return start
    if nums[end]<nums[end-1]:
        return end
    start += 1
    end -= 1
    while start<= end:
        center = (start+end) // 2
        if nums[center-1] >nums[center] and nums[center]<nums[center+1]:
            return center
        elif  nums[center-1]<nums[center]:
            end = center -1
        elif nums[center] > nums[center+1]:
            start = center+1
    

if __name__ == "__main__":
    nums = [2,1,5,7,3,4,6,8,9]
    print(getLocalMin(nums))