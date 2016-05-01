from collections import defaultdict
from text_splitter import FileSplitter

class raffle(object):

    def __init__(self,lotto_file):
        self.data = lotto_file

        lotto_splitter = FileSplitter(self.data)
        lines = lotto_splitter.split_text()
        #print lines
        for nums, jolly in enumerate(lines):
            print jolly*




if __name__ == "__main__":
    file_obj = raffle('lotto.txt')
