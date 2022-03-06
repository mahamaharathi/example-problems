def isPalindrome(strng):
    print(strng)
    if len(strng) < 2:
        return True
    if strng[0] == strng[-1]:
        print('1')
        print(len(strng[1:-1]))
        return isPalindrome(strng[1:-1])
    return False


print(isPalindrome('aaea'))
