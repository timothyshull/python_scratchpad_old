import subprocess
import re
import os
import pprint

cwd = os.getcwd()


def dmsetup_remove():
    p1 = subprocess.Popen(['ps', 'wwwaux'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
    dmsetup = p1.communicate()[0].splitlines()
    pprint.pprint(dmsetup)


def main():
    dmsetup_remove()


if __name__ == '__main__':
    main()
