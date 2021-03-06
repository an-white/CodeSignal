import re


def isIPv4Address(inputString):

    nums = inputString.split(".")
    if len(nums) != 4:
        return False

    nums = [n for n in nums if n != "" and not re.search("[^0-9]", n)]
    if len(nums) != 4:
        return False

    outliers = [x for x in nums if int(x) > 255 or int(x) < 0]
    if len(outliers) == 0:
        return True
    else:
        return False


isIPv4Address("172.16.254.1")
isIPv4Address("172.316.254.1")
isIPv4Address(".254.255.0")
