from collections import defaultdict
import json


class FileSplitter(object):

    def __init__(self,txt_file_name):

        self.data = txt_file_name


    def split_text(self,delimeter):

        line_data = defaultdict(list)
        with open(self.data, 'r') as infile:
             for ind, line in enumerate(infile):
                 line_data[ind].append(line.split(delimeter))
        return line_data


    def get_record(self,index,delimeter):

        elem = defaultdict(dict)
        content = self.split_text(delimeter)[index][0]

        elem['code'],elem['rag1'],elem['rag2'],elem['rag3'],elem['cog'],elem['nome'],elem['ind'], \
        elem['cap'],elem['loc'],elem['prov'],elem['tel1'],elem['tel2'],elem['fax'],elem['email'], \
        elem['piva'],elem['codfis'] = content

        return elem


    def get_records(self,delimeter):

        content = res =  defaultdict(list)
        content = self.split_text(delimeter)
        for i, val in enumerate(content):
                res[i] = self.get_record(i,delimeter)
        return res


    def json_record(self,index,delimeter):

        return json.dumps(self.get_record(index,delimeter))


    def json_records(self,delimeter):

         return json.dumps(self.get_records(delimeter))



if __name__ == "__main__":
    file_obj = FileSplitter('ANCLI_000024_2015.TXT')
    print (file_obj.json_records('|'))
    print (file_obj.json_record(0,'|'))
