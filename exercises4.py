'''
Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

'''

def vowelChecker(str_char):
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    if str_char.upper() in vowel_list:
        return True
    else:
        return False


print(vowelChecker('A'))

print(vowelChecker('B'))
