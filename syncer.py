import os
import time
import hashlib


def get_hash(path):
    _hash = hashlib.md5()
    with open(path, 'rb') as file:
        buf = file.read()
        _hash.update(buf)
    return _hash.hexdigest()


class Syncer:
    """get file's hash value and check file was changed"""
    def __init__(self, abs_path, path, _hash):
        self.abs_path = abs_path
        self.path = path
        self._hash = _hash

    def get_last_modified(self):
        """get time of recent content modification """
        modified = os.stat(self.abs_path)[8]
        return time.ctime(modified)        

    def file_changed(self, update):
        """if file changed return True else return False""" 
        new_hash = get_hash(self.abs_path)
        if new_hash is not self._hash:
            if update:
                self._hash = new_hash
            return True
        return False
    
    def is_file_exist(self):
        return os.path.exists(self.abs_path)