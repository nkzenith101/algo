# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear 
# in both lower and upper cases, more than once.

def reverseVowels(s: str) -> str:
    vovels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    vovels_in_string = []
    for i in s:

        if i in vovels:
            vovels_in_string.append(i)
    print(vovels_in_string)
    left = 0
    right = len(vovels_in_string)-1
    while left < right:
        vovels_in_string[left], vovels_in_string[right] = vovels_in_string[right], vovels_in_string[left]
        left += 1
        right -= 1
    new_s = list(s)
    j = 0
    for i in range(len(new_s)):
        if new_s[i] in vovels:
            new_s[i] = vovels_in_string[j]
            j += 1
    
    return ''.join(new_s)

print(reverseVowels(s="IceCreAm"))