# Given a string s, reverse the order of characters in each 
# word within a sentence while still preserving whitespace 
# and initial word order.

def reverseWords(s: str) -> str:
    s_list = list(s)
    left, right = 0, 0
    for i in range(len(s_list)):
        if s_list[i] == " " or i == len(s_list)-1:
            right = i-1 if s_list[i] == " " else i
            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            left,right = i+1,i+1 

    return "".join(s_list)

print(reverseWords(s = "Let's take LeetCode contest"))