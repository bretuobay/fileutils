


'''
The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively.
But suppose we have a much larger number of numbers, or suppose we cannot tell
in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

'''



def max_in_list(**kwargs):
    res = 0
    for ind, item in kwargs.items():
        if item > res:
            res = item
    return res



kwargs = {'1':2,'2':8,'3':30}

print(max_in_list(**kwargs))
