# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

def arithmeticTriplets(nums: list[int], diff: int) -> int:
    count = 0
    for i in range(len(nums)):
        left = i +1
        right = len(nums)-1
        while left < right:
            if nums[left] - nums[i] > diff:
                break
            if nums[left] - nums[i] < diff:
                left += 1
                continue
            if nums[right] - nums[left] > diff:
                right -= 1
            if nums[right] - nums[left] < diff:
                left += 1
            if (nums[left] - nums[i]) == diff and (nums[right] - nums[left]) == diff:
                print(i, left, right)
                count += 1
                left += 1
                right -= 1
            
    return count

print(arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
print(arithmeticTriplets(nums = [4,5,6,7,8,9], diff = 2))