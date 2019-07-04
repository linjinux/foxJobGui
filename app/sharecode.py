import os

#class all_directory():
#    def __init__(self):
#        pass
def root_app_directory():
    directory=os.path.abspath('.')
    print(directory)
    return directory
