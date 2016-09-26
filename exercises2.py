'''
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
'''
from exercises1 import max

# use function from previous exercise to shorten check
def max_of_three(num1,num2,num3):
    temp = max(num1,num2)
    return max(temp,num3)


def max_of_three1(a,y,z):
    Max = a
    if y > Max:
        Max = y
    if z > Max:
        Max = z
        if y > z:
            Max = y
    return Max



print ( max_of_three1(13,20.6,3) )
