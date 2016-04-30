from collections import defaultdict


class FileSplitter(object):

    def __init__(self,txt_file_name):
        self.data = txt_file_name


    def split_text(self):
        line_data = defaultdict(list)
        with open(self.data, 'r') as infile:
             for ind, line in enumerate(infile):
                 line_data[ind].append(line.split('|'))
        return line_data


    def get_record(self,index):

        elem = defaultdict(dict)
        content = self.split_text()[index][0]

        elem['code'],elem['rag1'],elem['rag2'],elem['rag3'],elem['cog'],elem['nome'],elem['ind'], \
        elem['cap'],elem['loc'],elem['prov'],elem['tel1'],elem['tel2'],elem['fax'],elem['email'], \
        elem['piva'],elem['codfis'] = content

        return elem


    def get_data_for_db(self):

         content = res =  defaultdict(list)
         content = self.split_text()
         for i, val in enumerate(content):
             res[i] = self.get_record(i)

         return res


if __name__ == "__main__":
    file_obj = FileSplitter('ANCLI_000024_2015.TXT')
    print file_obj.get_data_for_db()
    #print file_obj.get_record(0)
