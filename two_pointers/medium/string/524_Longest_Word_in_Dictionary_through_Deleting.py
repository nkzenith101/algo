# Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. 
# If there is more than one possible result, return the longest 
# word with the smallest lexicographical order. 
# If there is no possible result, return the empty string.

def findLongestWord(s: str, dictionary: list[str]) -> str:
    longest_word = ''
    for word in dictionary:
        left = 0
        right = 0
        temp_word = ''
        while right < len(word) and left < len(s):
            if word[right] == s[left]:
                temp_word+=word[right]
                left += 1
                right += 1
            else:
                left += 1
        if right == len(word):
            if len(temp_word) > len(longest_word):
                longest_word = temp_word
            elif len(temp_word) == len(longest_word):
                longest_word = min(longest_word, temp_word)
    return longest_word

print(findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))