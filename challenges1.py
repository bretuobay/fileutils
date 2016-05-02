

class CodeChallenge(object):

    '''
Question:
    Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    '''
    def Question1(self):
        data = range(10,40)
        res = []
        for i in data:
            if (i%7==0) and (i%5!=0):
                res.append(str(i))
        print (','.join(res)) # joins list  with comma, essentially comma separated file

    '''
     Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
    '''

    def Question2(self,num):
        self.num = num
        if self.num == 0:
            return 1
        else:
            temp_n = self.num
            self.num -= 1
            return temp_n * self.Question2(self.num) # alternatively, (self.n + 1)*self.factorial()


    '''
    With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    '''
    def Question3(self,num):
        self.num = num
        res = {}
        while(self.num>0):
            res[self.num] = self.num * self.num
            self.num = self.num -1
        return res

    '''

   Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

   '''
    def Question4(self):
        print('Please input numbers below:: ')
        values= input()
        l=values.split(",")
        t=tuple(l)
        print (l)
        print (t)



class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        print('Cursor waiting for input values::')
        self.s = input()

    def stringToLower(self):
        print (self.s.lower())
        print (self.s.upper())
