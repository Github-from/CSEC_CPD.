def compare_strings_ignore_case(str1, str2):
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    
    if str1_lower < str2_lower:
        return -1
    elif str1_lower > str2_lower:
        return 1
    else:
        return 0
str1 = input()
str2 = input()

result = compare_strings_ignore_case(str1, str2)
print(result)