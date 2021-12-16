def checkPalindrome(input_string):
    normal = input_string.lower()

    reverse = normal[-1::-1]

    return reverse == normal


print(checkPalindrome("aba"))
