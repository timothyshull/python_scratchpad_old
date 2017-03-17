class File:
    def __init__(self, filename, mode):
        print 'initializing'
        self.filename = filename
        self.mode = mode
        self.open_file = None

    def __enter__(self):
        print 'opening file'
        self.open_file = 'open_file'
        return self.open_file

    def __exit__(self, *args):
        self.open_file = None
        print 'exiting'
        print self.open_file


class AnotherClass:
    def test_method(self):
        print 'test method'


# files = []
# # for _ in range(10000):
# with File('foo.txt', 'w') as infile:
#     print infile
#     # infile.write('foo')
#     # files.append(infile)
#
# print 'after'
AnotherClass().test_method()
