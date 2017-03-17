import re
import subprocess
import pprint


def test_mount_grep():
    p1 = subprocess.Popen(['mount'], stdout=subprocess.PIPE)
    p1_stdout = p1.communicate()[0].splitlines()
    root_drive = None
    for line in p1_stdout:
        if ' / ' in line:
            mo = re.match(r'^(\S+)', line)
            if mo:
                root_drive = mo.group(0)
    print(root_drive)


def main():
    test_mount_grep()


if __name__ == '__main__':
    main()
