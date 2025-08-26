# Given a string s, return the longest palindromic substring in s.

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# O^3 is solution too, differnse between this two solutions - is speed, pay attention to additional operations (len, slices)
# def longestPalindrome(s: str) -> str:
#     longest_palindrome = ''
#     for i in range(len(s)):
#         temp_palindrome = ''
#         for j in range(i, len(s)):

#             if len(s[i:j+1]) < 2:
#                 temp_palindrome = s[i]
#             elif is_palindrome(token=s[i:j+1]):
#                 temp_palindrome = s[i:j+1]
#             if len(temp_palindrome) > len(longest_palindrome):
#                 longest_palindrome = temp_palindrome

            
#     return longest_palindrome

# def is_palindrome(token: str) -> bool:
#     i = 0
#     j = len(token)-1
    
#     while i<j:
#         if token[i] != token[j]:
#             return False
#         i += 1
#         j -= 1
#     return True

def longestPalindrome(self, s: str) -> str:
    if len(s) == 1:
        return s
    max_len=1
    max_str=s[0]
    for i in range(len(s)):
        for j in range(i, len(s)):
            if j-i+1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                max_len = j-i+1
                max_str = s[i:j+1]
    return max_str

print(longestPalindrome(s="bb"))