import os
import cmd
import glob
import importlib
import imp
from types import MethodType
from functools import partial


class TestCli(cmd.Cmd):
    TEST_STRING = 'this is my test'

    def __init__(self):
        cmd.Cmd.__init__(self)
        file_dir = os.path.abspath(os.path.dirname(__file__))
        print(file_dir)
        cmds = glob.glob('{0}/cli_cmds/*.py'.format(file_dir))
        self.cmd_files = [elem for elem in cmds if '__init__' not in elem]
        self.load_cmds()

    def load_cmds(self):
        for f in self.cmd_files:
            print(f)
            module_name, ext = os.path.splitext(os.path.basename(f))
            module_dir = os.path.dirname(f)
            module_file, module_path, description = imp.find_module(module_name, [module_dir])
            module = imp.load_module(module_name, module_file, f, ('', 'r', imp.PY_SOURCE))
            # print(dir(module))
            setattr(self, 'do_' + module_name, MethodType(module.CmdObject.__call__, self, TestCli))

    def do_print_self(self, *args):
        print(dir(self))

    # def do_call_callable(self, *args):
    #     self.callable_as_method()




# from types import MethodType
#
# class Foo(object):
#     def __init__(self):
#         pass
#
#     def __call__(self, *args, **kwargs):
#         pass
#
# class Bazz(object):
#     def __init__(self):
#         pass
#
# setattr(Bazz, 'test_method', MethodType(Foo(), None, Bazz))
#
# b = Bazz()
#     b.test_method()


if __name__ == '__main__':
    cli = TestCli()
    cli.cmdloop()
