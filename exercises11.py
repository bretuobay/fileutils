'''

Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx".
For the sake of the exercise you should ignore that the problem can be solved in this manner.)

'''
# easiste not prescribed

def generate_n_chars(_nchars,_char):
    return _nchars*_char



def generate_n_chars1(_nchars,_char):
    res = ''
    for i in range(1,_nchars):
        res += _char
    return res



# alternatively cast to list and then use join?
def generate_n_chars2(_nchars,_char):

    res = []
    for i in range(1,_nchars):

        res.append(_char) # add to list and then join - up later

    return "".join(res)



print(generate_n_chars2(10,'A'))
