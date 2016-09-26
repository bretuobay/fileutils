'''
Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise.
 (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)

'''

def is_member(neddle, hay):
    count = hay.count(neddle)
    if(count>0):
        return True
    else:
        return False




#print(is_member('lol','jajajajajjackjajajaj'))

# compare ints to ints not somthing else
#print(is_member(3,[2,3,4,45,3]))
