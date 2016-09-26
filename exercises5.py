'''
Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between.
For example, translate("this is fun") should return the string "tothohisos isos fofunon".

'''


def translate(str_input):
    vowel_list = ['A', 'E', 'I', 'O', 'U']
    temp = str_output = ''
   # TODO: remove when there are spaces 
    for char in str_input:
        if char.upper() not in vowel_list or char.isspace() == True :
            temp = char + 'o' + char
        else:
            temp = char
        str_output += temp

    return str_output



print (translate("this is fun"))
