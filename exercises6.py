'''
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a
 list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
 '''

def sum_list(input_list):
    res = 0
    for item in input_list:
        res +=item
    return res




def multiply(input_list):
    res = 1;
    for item in input_list:
        res *= item
    return res
#use sum_list not to cause confusion with inbuilt functions

print (sum_list([1, 2, 3, 4]))

print(multiply([1, 2, 3, 4]))
