'''
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

****
*********
*******

'''

def histogram(input_list):
    star_list = []
    for item in input_list:
        star_list.append(item*'*')
    for hist_line in star_list:
        print(hist_line)



histogram([4, 9, 7])
