from collections import defaultdict
from text_splitter import FileSplitter

class raffle(object):

    def __init__(self,lotto_file):
        self.data = lotto_file
        self.entries = defaultdict(list)
        lotto_splitter = FileSplitter(self.data)
        lines = lotto_splitter.split_text(',')
        num_line = len(lines)

        while(num_line>=0):
            for ind, row in enumerate(lines[num_line]):
                row[-1] = row[-1].rstrip('\n')
                self.entries[num_line] = row
            num_line = num_line - 1


    def get_all_entries(self):
        print (self.entries)


    def get_frequent(self):

        








if __name__ == "__main__":
    obj = raffle('lotto.txt')
    obj.get_frequent()
