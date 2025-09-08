# No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

# Given an integer n, return a list of two integers [a, b] where:

# a and b are No-Zero integers.
# a + b = n
# The test cases are generated so that there is at least one valid solution. 
# If there are many valid solutions, you can return any of them.

 

# Example 1:

# Input: n = 2
# Output: [1,1]
# Explanation: Let a = 1 and b = 1.
# Both a and b are no-zero integers, and a + b = 2 = n.

def getNoZeroIntegers(n: int) -> list[int]:
    for i in range(1,n):
        if '0' not in str(n-i) and '0' not in str(i):
            return [i, n-i]

print(getNoZeroIntegers(n=11))