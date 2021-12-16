def checkPalindrome(input_string):
    normal = input_string.lower()

    reverse = normal[::-1]

    return reverse == normal


print(checkPalindrome("aba"))

## lambda fucntion
checkPalindrome = lambda string: string == string[::-1]
