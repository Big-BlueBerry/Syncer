import syncer
import os 


# get syncer objects from first, second path
def scan(first, second):
    abs_first = [os.path.join(root, _file) for root, dirs, files in os.walk(first) for _file in files]
    abs_second = [os.path.join(root, _file) for root, dirs, files in os.walk(second) for _file in files]

    first_syncers = [syncer.Syncer(path, path.replace(first, ""), syncer.get_hash(path)) for path in abs_first]
    second_syncers = [syncer.Syncer(path, path.replace(second, ""), syncer.get_hash(path)) for path in abs_second]

    return first_syncers, second_syncers


# find different files doesn't same name
def compare_path(first, second):
    assert type(first[0]) == type(second[0]) == syncer.Syncer, 'Should insert Syncer Object'
    first_files = {_file.path: _file._hash for _file in first}
    second_files = {_file.path: _file._hash for _file in second}

    first_names = first_files.keys()
    second_names = second_files.keys()
    
    unexist_first = [x for x in first_names if not x in second_names]
    unexist_second = [x for x in second_names if not x in first_names]

    for x in unexist_first:
        print(x + " is not in second dir")
    for x in unexist_second:
        print(x + " is not in first dir")

# test
if __name__ == '__main__':
    first, second = scan('D:/Study/Syncer/test', 'C:/Users/dsm2016/Pictures/wallpaper')
    compare_path(first, second)
    