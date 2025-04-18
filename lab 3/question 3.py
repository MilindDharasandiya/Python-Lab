def is_substring(str1, str2):

    if len(str1) >= len(str2):
        long_str = str1
        short_str = str2
    else:
        long_str = str2
        short_str = str1

   
    for i in range(len(long_str) - len(short_str) + 1):
        match = True
        for j in range(len(short_str)):
            if long_str[i + j] != short_str[j]:
                match = False
                break
        if match:
            return True
    return False

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")


if is_substring(string1, string2):
    print("Yes, one string is present in the other.")
else:
    print("No, neither string is present in the other.")
