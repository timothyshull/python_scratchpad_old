#!/usr/bin/env python

import shutil
import os
import subprocess
import installer
from tempfile import mkstemp


def write_commit_to_config():
    base_project_dir = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'])
    installer_dir = '{0}/src/deploy/installer'.format(base_project_dir.strip())
    config_file = '{0}/config.py'.format(installer_dir)
    commit_out = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    commit_out = commit_out.strip()
    fd, abs_path = mkstemp()
    with open(abs_path, 'w') as tmp_file:
        with open(config_file) as src_file:
            for line in src_file:
                if 'GIT_COMMIT' in line:
                    tmp_file.write('GIT_COMMIT = \'{0}\'\n'.format(commit_out))
                else:
                    tmp_file.write(line)
    os.close(fd)
    os.remove(config_file)
    shutil.move(abs_path, config_file)


if __name__ == "__main__":
    write_commit_to_config()
