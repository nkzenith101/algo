# You are given a 2D 0-indexed integer array dimensions.

# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length 
# and dimensions[i][1] represents the width of the rectangle i.

# Return the area of the rectangle having the longest diagonal. If there are multiple 
# rectangles with the longest diagonal, return the area of the rectangle 
# having the maximum area.
from math import sqrt
def areaOfMaxDiagonal(dimensions: list[list[int]]) -> int:
    max_sqrt_idx = 0
    max_sqrt = 0
    max_dimension = 0
    for i in range(len(dimensions)):
        cur_sqrt = sqrt((dimensions[i][0]*dimensions[i][0] + dimensions[i][1]*dimensions[i][1]))
        cur_dimension = dimensions[i][0] * dimensions[i][1]
        if cur_sqrt > max_sqrt or (cur_sqrt == max_sqrt and cur_dimension > max_dimension):
            max_sqrt = cur_sqrt
            max_dimension = cur_dimension

    return max_dimension

print(areaOfMaxDiagonal(dimensions = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]))