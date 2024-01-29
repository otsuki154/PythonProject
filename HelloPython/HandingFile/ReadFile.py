import collections
try:
    file = open('../FileSamples/lyrics.txt', 'r')
    contents = file.read()
except FileNotFoundError:
    print('file not found. Please Thanh')
except PermissionError:
    print('please check file permission')
except ValueError:
    print('please check file contents')
except Exception as e:
    print(e)
else:
    words = contents.split() #tuong duong voi contents.split(' ')
    '''
    for word in words:
        print("{0}: {1}".format(word, words.count(word)))
    '''

    print(collections.Counter(words))