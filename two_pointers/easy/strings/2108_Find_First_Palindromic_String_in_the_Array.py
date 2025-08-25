# Given an array of strings words, return the first palindromic string in the array. 
# If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

def firstPalindrome(words: list[str]) -> str:
    for word in words:
        left=0
        right=len(word) - 1
        count=0
        if len(word) > 1:
            while left < right:
                if word[left]==word[right]:
                    count += 1
                if (len(word)%2==0 and count == len(word)/2) or ((len(word)-1)%2==0 and count == (len(word)-1)/2):
                    return word
                left += 1
                right -= 1
    return ""

print(firstPalindrome(words = ["xngla","e","itrn","y","s","pfp","rfd"]))