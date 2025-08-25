# You are given an m x n integer matrix grid, and three integers x, y, and k.

# The integers x and y represent the row and column indices of the top-left corner 
# of a square submatrix and the integer k represents the size (side length) 
# of the square submatrix.

# Your task is to flip the submatrix by reversing the order of its rows vertically.

# Return the updated matrix.

def reverseSubmatrix(grid: list[list[int]], x: int, y: int, k: int) -> list[list[int]]:
    start_x = x
    start_y = y
    end_x = x + k - 1
    end_y = y+k

    while start_x < end_x:
        start_y = y
        while start_y < end_y:
            print(grid[start_x][start_y], grid[end_x][start_y])
            grid[start_x][start_y], grid[end_x][start_y] = grid[end_x][start_y], grid[start_x][start_y]
            start_y += 1 
        start_x += 1
        end_x -= 1

    return grid

print(
    reverseSubmatrix(
        [[7,12],[19,3]], x = 0, y = 0, k = 1
    )
)