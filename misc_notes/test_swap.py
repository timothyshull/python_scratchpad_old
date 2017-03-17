#!/usr/bin/env python

import os
import cmd
import readline
import subprocess
import re

class ConsoleTwo(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "console2>> "
        self.intro = "Welcome to console!"  ## defaults to None

    ## Command definitions ##
    def do_hist(self, args):
        """Print a list of commands that have been entered"""
        print self._hist

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    ## Command definitions to support Cmd object functionality ##
    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(args)

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        subprocess.Popen(args)
        # os.system(args)

    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        ## The only reason to define this method is for the help text in the doc string
        cmd.Cmd.do_help(self, args)

    def do_ls(self, dir):
        args = dir.split() if dir else []
        print args 
        try:
            cmd = subprocess.Popen(['ls', dir], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = cmd.communicate()
            if out:
                out = re.sub(r'\Z', '', out, re.MULTILINE)
                print out
        except IOError:
            pass
        except KeyboardInterrupt:
            pass
            # return subprocess.Popen()

    def do_test_input(self, line):
        in_str = raw_input('Input a string: \n')
        print(in_str + line)
        in_str = raw_input('Input aother string: \n')
        print(in_str + line)

    ## Override methods in Cmd object ##
    def preloop(self):
        """Initialization before prompting user for commands.
           Despite the claims in the Cmd documentaion, Cmd.preloop() is not a stub.
        """
        cmd.Cmd.preloop(self)  ## sets up command completion
        self._hist = []  ## No history yet
        self._locals = {}  ## Initialize execution namespace for user
        self._globals = {}

    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)  ## Clean up command completion
        print "Exiting..."

    def precmd(self, line):
        """ This method is called after the line has been input but before
            it has been interpreted. If you want to modifdy the input line
            before execution (for example, variable substitution) do it here.
        """
        self._hist += [line.strip()]
        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.
           If you want to do some post command processing, do it here.
        """
        return stop

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        try:
            exec (line) in self._locals, self._globals
        except Exception, e:
            print e.__class__, ":", e


class ConsoleOne(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "console1>> "
        self.intro = "Welcome to console!"  ## defaults to None
        self._exit_val = None

    ## Command definitions ##
    def do_hist(self, args):
        """Print a list of commands that have been entered"""
        print self._hist

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    ## Command definitions to support Cmd object functionality ##
    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_exit(args)

    def do_exit_to_two(self, args):
        print args
        print 'in exit to two'
        self._exit_val = 'two'
        new_cmd = ConsoleTwo()
        new_cmd.cmdloop()
        # return 'two'

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        subprocess.Popen(args)
        # os.system(args)

    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        ## The only reason to define this method is for the help text in the doc string
        cmd.Cmd.do_help(self, args)

    def do_ls(self, dir):
        try:
            cmd = subprocess.Popen(['ls', dir], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = cmd.communicate()
            if out:
                out = re.sub(r'\Z', '', out, re.MULTILINE)
                print out
        except IOError:
            pass
        except KeyboardInterrupt:
            pass
            # return subprocess.Popen()

    def do_test_input(self, line):
        in_str = raw_input('Input a string: \n')
        print(in_str + line)
        in_str = raw_input('Input aother string: \n')
        print(in_str + line)

    ## Override methods in Cmd object ##
    def preloop(self):
        """Initialization before prompting user for commands.
           Despite the claims in the Cmd documentaion, Cmd.preloop() is not a stub.
        """
        cmd.Cmd.preloop(self)  ## sets up command completion
        self._hist = []  ## No history yet
        self._locals = {}  ## Initialize execution namespace for user
        self._globals = {}

    def postloop(self):
        """Take care of any unfinished business.
           Despite the claims in the Cmd documentaion, Cmd.postloop() is not a stub.
        """
        cmd.Cmd.postloop(self)  ## Clean up command completion
        print "Exiting..."
        return self._exit_val

    def precmd(self, line):
        """ This method is called after the line has been input but before
            it has been interpreted. If you want to modifdy the input line
            before execution (for example, variable substitution) do it here.
        """
        self._hist += [line.strip()]
        return line

    def postcmd(self, stop, line):
        """If you want to stop the console, return something that evaluates to true.
           If you want to do some post command processing, do it here.
        """
        return stop

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        try:
            exec (line) in self._locals, self._globals
        except Exception, e:
            print e.__class__, ":", e





if __name__ == '__main__':
    console = ConsoleOne()
    ret_val = console.cmdloop()
    print('in main')
    print ret_val
