# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

# For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
# Return the resulting string.

def reversePrefix(word: str, ch: str) -> str:
    new_word = list(word)
    anchor = None
    for i in range(len(new_word)):
        if new_word[i] == ch and not anchor:
            anchor = i
            left = 0
            right = i
            while left < right:
                new_word[left], new_word[right] = new_word[right], new_word[left]
                left += 1
                right -= 1
            break

    return ''.join(new_word)

print(reversePrefix(word = "abcdefd", ch = "d"))