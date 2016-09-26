'''
Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
'''
#since strings are iterable use a counter for this
#works for both strings and lists since python strings are list
def strLen(str_or_list):
    slen = 0
    for c in str_or_list:
         slen += 1
    return slen

##using inbuit lambda functions etc
def strLen1(str_or_list):
    return sum(map(lambda x:1, str_or_list))






print(strLen1('hjshjshjsjhshjshjsdhjshj'))

print(strLen1([1,2,3,4,5,5,6,7,7,7]))
