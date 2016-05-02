'''
        Tes the use of a dictionary to implment switeching operations in python
'''

class PySwitch(object):

        # define the function blocks
    def zero(self):
        print ("You typed zero.\n")

    def sqr(self):
        print ("n is a perfect square\n")

    def even(self):
        print ("n is an even number\n")

    '''def prime(self):
        print ("n is a prime number\n")
'''
    def test_options(self,option):
        return self.options[option]()

# map the inputs to the function blocks
    self.options = {
           0 : zero,
           1 : sqr,
           2 : even,
           3 : prime,
          }



if __name__ == '__main__':
    obj = PySwitch()
    obj.test_options(2)
