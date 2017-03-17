import subprocess
import re
import os
import pprint

cwd = os.getcwd()


def dmsetup_remove():
    p1 = subprocess.Popen(['/sbin/dmsetup', 'ls'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
    dmsetup = p1.communicate()[0]

    part_array = re.findall(r'(mpath[a-z]*p\d+)', dmsetup)

    for part in part_array:
        subprocess.call(['/sbin/dmsetup', 'remove', part])


def main():
    dmsetup_remove()


if __name__ == '__main__':
    main()
