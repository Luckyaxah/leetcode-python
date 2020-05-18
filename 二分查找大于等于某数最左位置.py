def findLeftNotLessThen(nums, num):
    left = 0
    right = len(nums)-1
    found = -1
    while left<=right:
        center = (left+right)//2
        if nums[center]>=num:
            found = center
            right = center-1
        else:
            left = center+1
    return found


if __name__ == "__main__":
    nums = [0,0,0,1,2,2,2,2,2,2,2,3,4,5,5,5]
    print(findLeftNotLessThen(nums,2))