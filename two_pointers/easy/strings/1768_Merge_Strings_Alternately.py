# You are given two strings word1 and word2. Merge the strings by adding 
# letters in alternating order, starting with word1. If a string is longer 
# than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def mergeAlternately(word1: str, word2: str) -> str:
    left, right, result = 0,0, ''
    while left < len(word1) and right < len(word2):
        result += word1[left] 
        result += word2[right]
        left += 1
        right += 1
    return result + word1[left:] + word2[right:]

print(mergeAlternately(word1 = "abcddd", word2 = "pqr"))
assert mergeAlternately(word1 = "abc", word2 = "pqr") == 'apbqcr'