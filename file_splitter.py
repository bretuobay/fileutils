
from collections import defaultdict


class FileSplitter(object):

    def __init__(self,txt_file_name):
        self.data = txt_file_name

    def splitFile1(self):
        line_data = {}
        with open(self.data, 'r') as infile:
             for line in infile:
                   row = line.split('|')
                   line_data['' + row[0] +''] = []
                   line_data['' + row[0] +''].append(row)
        return line_data

    def splitFile2(self):
        line_data = {}
        with open(self.data, 'r') as infile:
             for line in infile:
                   ind, content = line.split('|')[0], line.split('|')
                   line_data[ind] = []
                   line_data[ind].append(content)
        return line_data

    def get_record(self,index):
        elem = defaultdict(dict)
        content = self.split_text()[index][0]

        elem['code'],elem['rag1'],elem['rag2'],elem['rag3'],elem['cog'],elem['nome'],elem['ind'], \
        elem['cap'],elem['loc'],elem['prov'],elem['tel1'],elem['tel2'],elem['fax'],elem['email'], \
        elem['piva'],elem['codfis'] = content

        return elem


    def split_text(self):
        line_data = defaultdict(list)
        with open(self.data, 'r') as infile:
            for ind, line in enumerate(infile):
                line_data[ind].append(line.split('|'))
        return line_data




if __name__ == "__main__":
    file_obj = FileSplitter('ANCLI_000024_2015.TXT')
    #print file_obj.split_text()[0]
    print file_obj.get_record(1)
