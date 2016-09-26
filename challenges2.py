
import os

class DirectoryOps(object):


    def get_full_dir_path(self):

        return os.getcwd()

    def get_relative_file_path(self):

        return __file__

    def get_full_file_path(self):

         return os.path.realpath(__file__)

    def get_file_dir_and_name(self):

        res = path, filename = \
              os.path.split(self.get_full_file_path())

        return res

    def get_file_dir_only(self):
        
         return os.path.dirname(self.get_full_file_path())


if __name__ == '__main__':

    obj = DirectoryOps()

    print (obj.get_full_dir_path())
    print (obj.get_relative_file_path())
    print (obj.get_file_dir_and_name())
    print (obj.get_file_dir_only())
