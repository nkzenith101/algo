# For two strings s and t, we say "t divides s" 
# if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x 
# divides both str1 and str2.

def gcdOfStrings(str1: str, str2: str) -> str:
    if len(str1) > len(str2):
        if str2 in str1:
            return divide(divider_str=str2, str=str1)
        else:
            return ''
    else:
        if str1 in str2:
            return divide(divider_str=str1, str=str2)
        else:
            return ''

def divide(divider_str, str):
    left = 0
    right = 0
    if len(divider_str) == len(str):
        if divider_str == str:
            return divider_str
        else:
            return ''

    while len(divider_str) != len(str):
        if len(divider_str) == left:
            new_str = str[left:]
            if len(new_str) < len(divider_str):
                return divide(divider_str=new_str, str=divider_str)
            else:
                return divide(divider_str=divider_str, str=new_str)
        if divider_str[left] == str[right]:
            left += 1
            right += 1
        else:
            return ''
    return divider_str

print(gcdOfStrings(    str1="ABCDEF", 
    str2="ABC"))
#assert gcdOfStrings(str1 = "ABCABC", str2 = "ABC") == "ABC"
assert gcdOfStrings(
    str1="TAUXXTAUXXTAUXXTAUXXTAUXX", 
    str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
) == "TAUXX"
