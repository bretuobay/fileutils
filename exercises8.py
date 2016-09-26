'''
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.
'''
import string

def remove_punctuations(word):
    return "".join(i.lower() for i in word if i in string.ascii_letters)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    text = remove_punctuations(text)
    return text==reverse(text)

something = "Rise to vote, sir."

print(is_palindrome("radar"))


print(is_palindrome("haha"))


print(is_palindrome("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era"))

print(is_palindrome("A car, a man, a maraca"))
