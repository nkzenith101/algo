# You have an array of floating point numbers averages which is initially empty. 
# You are given an array nums of n integers where n is even.

# You repeat the following procedure n / 2 times:

# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.

def minimumAverage(nums: list[int]) -> float:
    res = float('inf')
    left = 0
    right = len(nums)-1
    nums.sort()
    while left < right:
        cur_average = (nums[left]+nums[right])/2
        res = min(cur_average,res)
        left += 1
        right -= 1
    return res
    

print(minimumAverage(nums = [7,8,3,4,15,13,4,1]))