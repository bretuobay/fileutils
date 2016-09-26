'''

Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function,
 or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.

 def outerInnerList(list1,list2):

     if len(list1) > len(list2):
         res = out, inner = list1, list2
     else:
         res = out, inner = list2, list1

     return res

 def overlapping(list1,list2):
     #use len to establish longer list
     outer, inner = outerInnerList(list1,list2)
     exist_list = []

     for in_item in inner:

         if is_member(in_item,outer):
             exist_list.append(True)
         else:
             exist_list.append(False)

     return True in  exist_list
     #return exist_list


 '''

from exercises9 import is_member


def overLapChecker(list1,list2):

    exist_list = []

    if len(list1) > len(list2):
        res = outer, inner = list1, list2
    else:
        res = outer, inner = list2, list1

    for in_item in inner:
        if is_member(in_item,outer):
            exist_list.append(True)
        else:
            exist_list.append(False)

    return True in  exist_list

# cleaner solutions ie more pythonic ways
def PythonicOverLapChecker1(list1,list2):

    return bool(set(list1) & set(list2))

def PythonicOverLapChecker2(list1,list2):
    # NB: this returns the inverse, disjoint sets True means no items found
    # not a very intuitive solution
    return not set(list1).isdisjoint(list2)



print(PythonicOverLapChecker2([1,2,23,4,5,2,4,5],[11,3,41,21]))
