# You are given an integer array height of length n. There are n vertical lines drawn 
# such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container 
# contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

def maxArea(height: list[int]) -> int:
    left=0
    right = len(height)-1
    max_water = 0
    while left < right:
        max_heigh = min(height[left], height[right])
        cur_container = max_heigh*(right-left)
        max_water = max(max_water, cur_container)
        if height[left] > height[right]:
            right -=1
        else:
            left += 1
    return max_water


print(maxArea(height = [1,8,6,2,5,4,8,3,7]))