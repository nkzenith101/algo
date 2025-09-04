# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    used = set()
    #print(nums)
    result = []
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            summary = nums[i] + nums[left] + nums[right]
            if summary == 0:
                if f'{nums[i]}{nums[left]}{nums[right]}' not in used:
                    result.append([nums[i], nums[left], nums[right]])
                    used.add(f'{nums[i]}{nums[left]}{nums[right]}')
                right -= 1
                left += 1
            elif summary > 0:
                right -= 1
            elif summary < 0:
                left += 1
    return result

print(threeSum(nums = [-1,0,1,2,-1,-4]))