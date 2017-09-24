import hashlib 


# test
if __name__ == '__main__':
    path = "test.txt"

    hasher = hashlib.md5()
    with open(path, 'rb') as file:
        buf = file.read()
        hasher.update(buf)

    print(hasher.hexdigest())
