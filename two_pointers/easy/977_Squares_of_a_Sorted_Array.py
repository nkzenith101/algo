# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

def sortedSquares(nums: list[int]) -> list[int]:
    sorted_squares = [0] * (len(nums))
    sorted_index = len(nums)-1
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left]*nums[left] > nums[right] * nums[right]:
            sorted_squares[sorted_index]=(nums[left]*nums[left])
            left += 1
            sorted_index -= 1
        elif nums[left]*nums[left] < nums[right] * nums[right]:
            sorted_squares[sorted_index]=(nums[right]*nums[right])
            right -= 1
            sorted_index -= 1
        elif nums[left]*nums[left] == nums[right] * nums[right]:
            sorted_squares[sorted_index]=(nums[right]*nums[right])
            sorted_index -= 1
            sorted_squares[sorted_index]=(nums[left]*nums[left])
            sorted_index -= 1
            left += 1
            right -= 1
    return sorted_squares
    
    

print(sortedSquares(nums = [-4,-1,0,3,10]))