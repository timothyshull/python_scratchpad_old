#!/usr/bin/env python

# import re
# import os
#
# with open(os.path.join(os.getcwd(), 'test_sudo.py'), 'r') as f:
#     print 'running'
#     contents = f.readlines()
#     for l in contents:
#         mo = re.search('[^#]*if\se\[0\]\s==\serrno', l)
#         if mo:
#             print(mo.group(0))
#             # print(mo.group(1))


# !/opt/bin/python2.7

import os
import sys
import grp
import pwd
import re
import subprocess


def validate_passwordless_sudo():
    cuid = os.geteuid()
    username = getattr(pwd.getpwuid(cuid), 'pw_name')
    err_msg = 'The group \'users\' must exist and it must be granted passwordless \'sudo\' privileges assigned in ' \
              '\'/etc/sudoers\'.\n Additionally, the current user, \'{0}\', must be assigned to the \'users\' group ' \
              'and be granted passwordless \'sudo\' in \'/etc/sudoers\'.'.format(username)

    # check to make sure the 'users' group exists
    try:
        grp.getgrnam('users')
    except KeyError:
        print >> sys.stderr, err_msg
        sys.exit(1)

    # open('/etc/sudoers') returns EACCES
    try:
        out = subprocess.check_output(['sudo', 'cat', '/etc/sudoers'])
    except subprocess.CalledProcessError:
        print >> sys.stderr, err_msg
        sys.exit(1)

    print(out)

    grp_has_privileges = False
    usr_has_privileges = False
    for l in out.splitlines():
        # '%users ALL=NOPASSWD: ALL'
        mo = re.search('[^#]*%users\s*?ALL\s*?=\s*?NOPASSWD:\s*?ALL', l, re.DOTALL)
        if mo:
            grp_has_privileges = True
        else:
            # '%users\s+ALL\s+?=\s+?({0})\s+?NOPASSWD:\s+?ALL'.format(username)
            user_search_string = '[^#]*%users\s?ALL\s?=\s?\\({0}\\)\s?NOPASSWD:\s?ALL'.format(username)
            mo = re.search(user_search_string, out, re.DOTALL)

        if mo:
            usr_has_privileges = True

    if not grp_has_privileges or not usr_has_privileges:
        print >> sys.stderr, err_msg
        sys.exit(1)


if __name__ == '__main__':
    validate_passwordless_sudo()
    print 'success'
