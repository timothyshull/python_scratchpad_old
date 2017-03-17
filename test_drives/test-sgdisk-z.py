import subprocess
import re
import os
import pprint

cwd = os.getcwd()


# TODO: possibly pass input as dict
def sgdisk_z(metadata):
    drv_arr = fdisk_drives.keys().sort()

    for drive in drv_arr:
        cond1 = re.search(r'/dev/mapper', drive) and not re.search(r'mpath', drive)
        cond2 = re.search(r'/dev/mapper', drive) and re.search(r'p[0-9]+$', drive)
        cond3 = '/dev/%s' % metadata['system_part'] == drive
        if not cond1 and not cond2 and not cond3:
            subprocess.call(['dd', 'if=/dev/zero', 'of=%s' % drive, 'bs==1M', 'count=16'])
            subprocess.call(['/usr/sbin/sgdisk', '-Z', drive])
            subprocess.call(['/usr/sbin/sgdisk', '-Z', drive])  # why run twice?


def main():
    dmsetup_remove()


if __name__ == '__main__':
    main()
