'''
        Tes the use of a dictionary to implment switeching operations in python
'''

class PySwitch(object):
    options = {}
        # define the function blocks
    def zero(self):
        print ("You typed zero.\n")

    def sqr(self):
        print ("n is a perfect square\n")

    def even(self):
        print ("n is an even number\n")

    def prime(self):
        print ("n is a prime number\n")

    def string_to_num(self,string):

        try:
            return int(string)
        except ValueError:
            return float(string)

# map the inputs to the function blocks, uses ints as
# dictionary keys, TODO : generalize for all dicts
    options = {
           0 : zero,
           1 : sqr,
           2 : even,
           3 : prime,
          }

    def test_options(self,option):

        if option in self.options:
            return self.options[option](self)
        else:
            print("option not available")




if __name__ == '__main__':
    obj = PySwitch()

    print("Please input option::")
    option = input()
    while option != '10':
        print("Please input option::")
        option = input()
        obj.test_options(obj.string_to_num(option))
