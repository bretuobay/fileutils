from collections import defaultdict
from text_splitter import FileSplitter
import json

class raffle(object):

    def __init__(self,lotto_file):
        self.data = lotto_file



    def split_lotto_file(self,delimeter):
        list_dict = defaultdict(dict)
        lotto_splitter = FileSplitter(self.data)
        return lotto_splitter.split_text(delimeter)


    def lotto_to_json(self):
        print json.dumps(self.split_lotto_file('|'))


    def merge_dicts(self,*dict_args):
        '''
        Given any number of dicts, shallow copy and merge into a new dict,
        precedence goes to key value pairs in latter dicts. to merge dictionaries

        '''
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result

    def get_bigger_dict(self,dict1,dict2):

        if( len(dict1) > len(dict2) ):
            res = bdict,sdict = dict1,dict2
        else:
            res = bdict,sdict = dict2,dict1
        return res


    def get_dict_diff(self,dict1,dict2):
        ''' this returns values and keys'''

        bdict, sdict = self.get_bigger_dict(dict1,dict2)
        ret_dict = {}
        for key,val in bdict.items():
            if sdict.has_key(key):
                if sdict[key] != val:
                    ret_dict[key] = [val,sdict[key]]
                else:
                    ret_dict[key] = [val]

        for key,val in sdict.items():
            ret_dict.setdefault(key,[val])
        return ret_dict

        ''' get keys that are not in the bigger dictionary
             what happends at the reverse
        '''
    def get_dict_diff1(self,dict1,dict2):

        bdict, sdict = self.get_bigger_dict(dict1,dict2)

        return [x for x in sdict.keys() if x not in bdict.keys()]

    def get_dict_diff1(self,dict1,dict2):

        bdict, sdict = self.get_bigger_dict(dict1,dict2)

        return [x for x in bdict.keys() if x not in sdict.keys()]



if __name__ == "__main__":
    obj = raffle('lotto.txt')
    '''
    print obj.merge_dicts({'ints':'7,34,34', 'floats':'3.4,45.3'}, \
                        {'old':'90,87,10', 'young':'3,7'})
    '''

    print obj.get_dict_diff1({'ints':'7,34,34', 'floats':'3.4,45.3','string':'4sdsddsdsdssd'}, \
                        {'old':'90,87,10', 'young':'3,7'})
