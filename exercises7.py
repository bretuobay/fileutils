'''
Define a function reverse() that computes the reversal of a string. For example, reverse("I am testing") should return the string
                "gnitset ma I".
'''
# this works by slicing from the end
#This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.
def reverse(input_str):
    return input_str[::-1]


print(reverse("I am testing"))
