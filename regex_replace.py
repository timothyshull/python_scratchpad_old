import glob
import re
import os
import tempfile
import shutil


def convert():
    all_files = glob.glob('{0}/*.hs'.format(os.getcwd()))

    for hs_f in all_files:
        tmp_file = None
        with open(hs_f, 'r') as f:
            all_text = f.read()

            match = re.search('```haskell\n([^`]*)```.*', all_text, re.DOTALL)

            if match:
                fd, tmp_path = tempfile.mkstemp()
                tmp_file = tmp_path
                with open(tmp_path, 'w') as tmp:
                    tmp.write(match.group(1))

        if tmp_file and os.path.isfile(os.path.abspath(tmp_file)):
            shutil.move(tmp_file, hs_f)
            # os.remove(tmp_file)


if __name__ == '__main__':
    convert()
