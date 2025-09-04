# Given an integer array nums of length n and an integer target, find three 
# integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

def threeSumClosest(nums: list[int], target: int) -> int:
    closest = float('inf')
    res = 0
    nums.sort()
    #print(nums)
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1

        while left < right:
            
            cur_sum = nums[i] + nums[left] + nums[right]
            
            length = abs(target-cur_sum)
            #print(nums[i], nums[left], nums[right], length)
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            elif cur_sum == target:
                return cur_sum
            
            if length < closest:
                
                closest = length
                res = cur_sum

    return res

print(threeSumClosest(nums = [10,20,30,40,50,60,70,80,90], target = 1))