def findIndices(nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
    for i in range(0, len(nums)-indexDifference):
        for j in range(i+indexDifference, len(nums)):
            if abs(nums[i]-nums[j]) >= valueDifference:
                return [i,j]
    return [-1,-1]

print(findIndices(nums = [1,2,3], indexDifference = 2, valueDifference = 4))