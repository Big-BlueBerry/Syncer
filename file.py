import os, time


class File:
    def __init__(self, name, path, hash):
        self.name = name
        self.path = path
        self.hash = hash

    def get_last_modified(self):
        # get time of recent content modification
        modified = os.stat(self.path)[8]    
        return time.ctime(modified)