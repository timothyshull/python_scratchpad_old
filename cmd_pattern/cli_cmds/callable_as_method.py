from types import MethodType


class CmdObject(object):
    CMD_TEST_STRING = 'test cmd string'

    def __init__(self):
        pass

    @staticmethod
    def __call__(self, *args, **kwargs):
        print('in callable as method')
        print(dir(self))
        print(self.TEST_STRING)

    @staticmethod
    def execute(self, *args, **kwargs):
        print('in callable as method')
        print(dir(self))


# class Bazz(object):
#     def __init__(self):
#         pass
#
#
# setattr(Bazz, 'test_method', MethodType(Foo(), None, Bazz))
#
# # b = Bazz()
# # b.test_method()
#
# __all__ = ['Foo']
