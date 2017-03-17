import subprocess
import re
import os
import pprint


test_str = """Disk /dev/sda: 21.5 GB, 21474836480 bytes, 41943040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x00030e04

   Device Boot      Start         End      Blocks   Id  System
Disk /dev/sda1:   *        2048      616447      307200   83  Linux
Disk /dev/sda2:          616448     4810751     2097152   82  Linux swap / Solaris
/dev/sda3         4810752    41943039    18566144   83  Linux"""

#TODO: the findall regex matches on both /dev/sda and /dev/sda1

def fdisk_drives():
    return_dict = {}
    p1 = subprocess.Popen(['fdisk', '-l'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=cwd)
    drives = p1.communicate()[0]

    filtered_drives = re.findall(r'Disk\s+(/dev/\S+):', drives)

    for elt in filtered_drives:
        short_elt = re.sub(r'/dev/', '', elt)
        if str(gettext_chomp('/sys/block/%s/removable' % short_elt)):
            continue
        if str(gettext_chomp('/sys/block/%s/ro' % short_elt)):
            continue
        if ignore_dev(short_elt):
            continue
        return_dict[elt] = 1

    pprint.pprint(return_dict)
    return return_dict



    # for part in part_array:
    #     subprocess.call(['/sbin/dmsetup', 'remove', part])


def main():
    fdisk_drives()

if __name__ == '__main__':
    main()
