import glob
import os
import shutil


def convert_files():
    cwd = os.getcwd()
    all_files = glob.glob('{0}/*.md'.format(cwd))
    for f in all_files:
        # print(f)
        shutil.move(f, '{0}/{1}.hs'.format(cwd, os.path.basename(f)[:-3]))


if __name__ == '__main__':
    convert_files()
